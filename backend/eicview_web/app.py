import os
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object(__name__)

# Path to our vault
if "EICVIEW_VAULT_PATH" in os.environ.keys():
    vault_path = os.environ["EICVIEW_VAULT_PATH"]
else:
    this_file_path = os.path.dirname(os.path.abspath(__file__))
    vault_path = os.path.abspath(os.path.join(this_file_path, "..", "..", "tmp"))

app.config["vault_path"] = vault_path

@app.before_request
def before_request():
    """Runs before any requiest"""
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

    return render_template("index.html", test_int=5, test_str="Ha ha ha", test_array=["Dog", "Cat", "Rat"])


# register modules
from statistics.views import mod as statistics_module

app.register_blueprint(statistics_module)

if __name__ == "__main__":
    app.run(debug=True)