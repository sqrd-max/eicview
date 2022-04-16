import gitlab
import zipfile
import os
import sys
import pathlib


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
    artifacts_expier = job.artifacts_expire_at
    status = job.status

    print(status)

    pathlib.Path(get_directory_name(base_path, project_id, branch, pipeline_id, job_id)).mkdir(parents=True, exist_ok=True)
    
    

    # job = project.jobs.get(report_job.id, lazy=True)
    # file_name = '__artifacts.zip'
    # with open(file_name, "wb") as f:
    #      job.artifacts(streamed=True, action=f.write)
    # zip = zipfile.ZipFile(file_name)
    # zip.extractall()

    # make directories
    # https://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python


def process_pipeline(pipeline, base_path):
    """Downloads all things from a pipeline"""

    jobs = pipeline.jobs.list(per_page=100)
    print(f"Pipeline has {len(jobs)} ")

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


def save_available_artifacts(project, num_pipelines=500):
    """...."""
    pipelines = project.pipelines.list()   # <= do paging to load ALL requiested pipelines
    for pipeline in pipelines:
        process_pipeline(pipeline)


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

    save_latest_artifacts(project, base_path)
    

