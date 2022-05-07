import gitlab
import zipfile
import os
import sys
import pathlib
import datetime
import logging
from pprint import pprint


is_sim = False
# is_verbose = True
logging.basicConfig(level=logging.INFO)

def get_directory_name(base_path, project_id, branch, pipeline_id, job_id):
    """Gets the right path to store artifacts"""
    return os.path.join(str(base_path), str(project_id), str(branch), str(pipeline_id), str(job_id))


def save_artifacts(job, pipeline, base_path):
    """Saves artifacts having a job object"""
    
    # extracting values
    project_id = job.project_id
    pipeline_id = job.pipeline['id']
    branch = job.pipeline['ref']
    job_expire_str = job.artifacts_expire_at

    # >oO degging
    # if is_verbose:
    #     print(f"  Saving artifacts... job id={job.id} status='{job.status}' branch='{branch}'")
    logging.info(f"Saving artifacts... job id={job.id} status='{job.status}' branch='{branch}'")
    
    # Filtration by job status
    if job.status != 'success':
        return

    # Check if expiration time exists at all (no artifacts if not)
    if not job_expire_str:    
        # if is_verbose:    
        #     print("    No expire time. Skipping job ")
        logging.debug("    No expire time. Skipping job ")
        return    
        
    # Check expiration time
    expire_time = datetime.datetime.strptime(job_expire_str, '%Y-%m-%dT%H:%M:%S.%fZ')

    
    current_datetime = datetime.datetime.now()
    time_left = expire_time - current_datetime
    if expire_time < current_datetime:
        # if is_verbose:
            #  print(f"    Artifacts are expired, expiration time = {expire_time} time gone {time_left}")
        logging.debug(f"Artifacts are expired, expiration time = {expire_time} time gone {time_left}")
        return

    # Ensure the directory exists
    dir_name = get_directory_name(base_path, project_id, branch, pipeline_id, job.id)
    pathlib.Path(dir_name).mkdir(parents=True, exist_ok=True)

    if not is_sim:
        # Not a simulation. Download files
        job = project.jobs.get(job.id, lazy=True)
        file_full_path = os.path.join(dir_name, 'artifacts.zip')
        with open(file_full_path, "wb") as f:
            job.artifacts(streamed=True, action=f.write)
        zip = zipfile.ZipFile(file_full_path)
        zip.extractall(dir_name)
        # if is_verbose:
            # print(f"    Saved successfully")
        logging.info("Saved successfully")
    else:
        # if is_verbose:
        #     print(f"    Simulated download and save")
        logging.info("Simulated download and save")


    # make directories
    # https://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python

    

def process_pipeline(pipeline, base_path):
    """Downloads all things from a pipeline"""

    jobs = pipeline.jobs.list(per_page=100)
    print(f"Processing pipeline id={pipeline.id} has {len(jobs)} jobs and status: '{pipeline.status}'")

    report_job = None
    for job in jobs:
        print(job.name)
        if job.name=="report":
            report_job = job     # How to do it without this for search
            break

    if not report_job:
        print("  No report job found")
    else:
        save_artifacts(report_job, pipeline, base_path)


def save_pipelines(project, base_path, arts_count=0):
    """
    @arts_count=0 - load all, else number of latest pipelines to process
    """

    # Documentation about list
    # https://python-gitlab.readthedocs.io/en/stable/api/gitlab.html#gitlab.mixins.ListMixin
    pipelines = project.pipelines.list(as_list=False)   # <= do paging to load ALL requiested pipelines
    
    for i, pipeline in enumerate(pipelines):
        if arts_count!=0 and i >= arts_count:
            break
        process_pipeline(pipeline, base_path)



def save_latest_artifacts(project, base_path):
    """..."""
    pipelines = project.pipelines.list()

    # Pipelines are sorted by date, so this is the latest pipeline
    pipeline = pipelines[0]
    process_pipeline(pipeline, base_path)


if __name__ == "__main__":

    # This file path
    print("This file path is:")

    if "EICVIEW_VAULT_PATH" in os.environ.keys():
        base_path = os.environ["EICVIEW_VAULT_PATH"]
    else:
        this_file_path = os.path.dirname(os.path.abspath(__file__))
        base_path = os.path.join(this_file_path, "..", "..", "tmp")

    print(base_path)
    print(sys.argv)
    
    # anonymous read-only access for public resources (GitLab.com)
    gl = gitlab.Gitlab()

    # anonymous read-only access for public resources (self-hosted GitLab instance)
    gl = gitlab.Gitlab('https://eicweb.phy.anl.gov/')

    # get project
    project_id = 473             # Detector athena
    project = gl.projects.get(project_id)
    
    print("Program arguments:")
    pprint(sys.argv)

    # TODO analyse sys.argv 
    # -s --simulate - not really artifacts to file
    # -v --verbose

    # arts_download.py --all -> download all pipelenes 500 = all
    # arts_download.py --all 5 -> download 5 last pielines
    # arts_download.py -> download only latest pipeline
    # arts_download.py --id 345 -> download pipeline id=345
    

    if "-s" in sys.argv or "--simulate" in sys.argv:
        print("Simulation mode")
        is_sim = True

    if "-v" in sys.argv or "--verbose" in sys.argv:
        print("Verbose mode")
        is_verbose = True

    # save_latest_artifacts(project, base_path)
    save_pipelines(project, base_path, 45)
