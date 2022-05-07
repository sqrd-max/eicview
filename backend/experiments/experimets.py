# This file path
import gitlab
import zipfile
import os
import sys
import pathlib
import datetime
import time

if __name__ == "__main__":   
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

    start = time.time()
    pipelines = project.pipelines.list(as_list=False) #all=True) #as_list=False)
        
    for i, pipeline in enumerate(pipelines):
        print(f"{i:<10} {pipeline.id}")
        if i >= 500:
            break
        
    print(f"Load done in {time.time() - start} sec")
