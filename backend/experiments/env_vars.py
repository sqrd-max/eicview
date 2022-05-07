import os

if "EICVIEW_VAULT_PATH" in os.environ.keys():
    base_path = os.environ["EICVIEW_VAULT_PATH"]
else:
    this_file_path = os.path.dirname(os.path.abspath(__file__))
    base_path = os.path.abspath(os.path.join(this_file_path, "..", "..", "tmp"))

print(base_path)