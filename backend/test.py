import gitlab
import zipfile
import os

print("This file path is:")
this_file_path = os.path.dirname(os.path.abspath(__file__))
print(os.path.join(this_file_path, "..", "tmp"))


# anonymous read-only access for public resources (GitLab.com)
gl = gitlab.Gitlab()

# anonymous read-only access for public resources (self-hosted GitLab instance)
gl = gitlab.Gitlab('https://eicweb.phy.anl.gov/')

# get project
project_id = 473             # Detector athena
project = gl.projects.get(project_id)

# print(project)
# print(f"{project.name}")

pipelines = project.pipelines.list()



# for pipeline in pipelines:
#    print(f"id: {pipeline.id:<8} status: {pipeline.status:<8} updated: {pipeline.updated_at}")

pipeline = pipelines[0]
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

    job = project.jobs.get(report_job.id, lazy=True)
    file_name = '__artifacts.zip'
    with open(file_name, "wb") as f:
         job.artifacts(streamed=True, action=f.write)
    zip = zipfile.ZipFile(file_name)
    zip.extractall()
    #zipfn = "___artifacts.zip"
    #print(report_job.artifacts(streamed=True))
    # with open(zipfn, "wb") as f:
    #     report_job.artifacts(streamed=True, action=f.write)

# example:
# Get a single artifact file by branch and job:
# project.artifacts.raw('branch', 'path/to/file', 'job')