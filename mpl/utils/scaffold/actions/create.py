import os
import json

def empty_file(path, file_name):
    with open(os.path.join(path, file_name), "w") as f:
        pass


def json_file(path, file_name, content):
    with open(os.path.join(path, file_name), "w") as f:
        json.dump(content, f)


def empty_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)