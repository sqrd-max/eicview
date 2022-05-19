import os
from datetime import datetime
from flask import Flask, render_template
from numpy import average

app = Flask(__name__)
app.config.from_object(__name__)

# Path to our vault
if "EICVIEW_VAULT_PATH" in os.environ.keys():
    vault_path = os.environ["EICVIEW_VAULT_PATH"]
else:
    this_file_path = os.path.dirname(os.path.abspath(__file__))
    vault_path = os.path.abspath(os.path.join(this_file_path, "..", "..", "tmp"))

app.config["vault_path"] = vault_path
app.config["this_file_path"] = this_file_path

@app.before_request
def before_request():
    """Runs before any request"""
    pass


@app.teardown_request
def teardown_request(exception):
    """Runs after everything"""
    pass


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')


@app.route('/sample')
def sample():
    return render_template('index.html')


@app.route('/')
def index():

    from pathlib import Path

    def folder_size(vault_path):
        size = 0
        numfile = 0 
        for file in Path(vault_path).rglob('*'):
            if (os.path.isfile(file)):
                size += os.path.getsize(file)
                numfile +=1
        return size, numfile

    
    def dir_num(this_file_path):
        dirnum = 0
        path = this_file_path
        for lists in os.listdir(path):
            sub_path = os.path.join(path, lists)
            if os.path.isdir(sub_path):
                dirnum = dirnum+1
        return dirnum


    size, numfile = folder_size(vault_path)
    dirnum = dir_num(this_file_path)

    average_folder_size = '%.2f' % ((size / (dirnum-1)) / 1048576)
    size = '%.2f' % (size / 1048576)

    # return f'artifacts quantity: {numfile} <br> folder size: {size} Mb <br> director: {dirnum}'
    return render_template("index.html",  file_quantity = numfile, file_size = size, dir_quantity = dirnum, average_folder_size = average_folder_size)

    

# register modules
from statistics.views import mod as statistics_module

app.register_blueprint(statistics_module)

if __name__ == "__main__":
    app.run(debug=True)