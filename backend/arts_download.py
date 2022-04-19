import gitlab
import zipfile
import os
import sys
import pathlib
import datetime


def get_directory_name(base_path, project_id, branch, pipeline_id, job_id):
    """Gets the right path to store artifacts"""
    return os.path.join(str(base_path), str(project_id), str(branch), str(pipeline_id), str(job_id))


def save_artifacts(job, base_path):
    """Saves artifacts having a job object"""

    # print(job)
    project_id = job.project_id
    pipeline_id = job.pipeline['id']
    branch = job.pipeline['ref']
    job_id = job.id
    status = job.status

    artifacts_expire_at = datetime.datetime.strptime(job.artifacts_expire_at, '%Y-%m-%dT%H:%M:%S.%fZ')
    current_datetime = datetime.datetime.now()

    artifacts_expire_in = artifacts_expire_at - current_datetime
    


    if artifacts_expire_at > current_datetime:

        dir_name = get_directory_name(base_path, project_id, branch, pipeline_id, job_id)
        pathlib.Path(dir_name).mkdir(parents=True, exist_ok=True)
        
        print(artifacts_expire_in)

        job = project.jobs.get(job.id, lazy=True)
        file_name = '__artifacts.zip'
        FileFullPath = os.path.join(dir_name, file_name)
        with open(FileFullPath, "wb") as f:
            job.artifacts(streamed=True, action=f.write)
        zip = zipfile.ZipFile(FileFullPath)
        # zip.extractall(dir_name)
    else:
        print(f"artifacts expired at {artifacts_expire_at}")

    # make directories
    # https://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python


def process_pipeline(pipeline, base_path):
    """Downloads all things from a pipeline"""

    jobs = pipeline.jobs.list(per_page=100)
    print(f"Pipeline has {len(jobs)} jobs ")

    report_job = None
    for job in jobs:
        print(job.name)
        if job.name=="report":
            report_job = job     # How to do it without this for search
            break

    if not report_job:
        print("No report job found")
    else:
        print(f"Report job id={report_job.id}")

        save_artifacts(report_job, base_path)


def save_available_artifacts(project):
    """...."""
    pipelines = project.pipelines.list(as_list=False)   # <= do paging to load ALL requiested pipelines
    for pipeline in pipelines:
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
    this_file_path = os.path.dirname(os.path.abspath(__file__))

    base_path = os.path.join(this_file_path, "..", "tmp")
    print(base_path)
    print(sys.argv)
    
    # anonymous read-only access for public resources (GitLab.com)
    gl = gitlab.Gitlab()

    # anonymous read-only access for public resources (self-hosted GitLab instance)
    gl = gitlab.Gitlab('https://eicweb.phy.anl.gov/')

    # get project
    project_id = 473             # Detector athena
    project = gl.projects.get(project_id)

    # TODO analyse sys.argv 
    # arts_download.py --all -> download all pipelenes 500 = all
    # arts_download.py --all 5 -> download 5 last pielines
    # arts_download.py -> download only latest pipeline
    # arts_download.py --id 345 -> download pipeline id=345

    # save_latest_artifacts(project, base_path)
    save_available_artifacts(project, base_path)

# Report job id=619168 упал тут