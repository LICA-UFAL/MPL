import json

def read_file_to_dict(file_path):
    """ 
    Read an file and convert to dict 
    Accepted formats : json.

    """
    response_dict = None
    with open(file_path, "r") as f:
        response_dict = json.load(f)

    return response_dict