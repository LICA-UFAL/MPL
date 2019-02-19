import os

SCAFFOLD_PROJECTS_PATH = "mpl/scaffolds/"

def create_project():
    pass

def get_scaffolds():
    """ Return an list of project scaffold paths """
    return [SCAFFOLD_PROJECTS_PATH + file_name for file_name in os.listdir(SCAFFOLD_PROJECTS_PATH)]
