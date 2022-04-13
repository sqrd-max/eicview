import os

def get_directory_name(base_path, project_id, branch, pipeline_id, job_id):
    return os.path.join(str(base_path), str(project_id), str(branch), str(pipeline_id), str(job_id))


if __name__ == "__main__":
    print(get_directory_name(os.curdir, 473, "master", 30000, 1000000))

