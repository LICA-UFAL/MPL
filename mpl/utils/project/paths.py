from mpl.settings import SCAFFOLDS_FOLDER_PATH, MPL_CACHE_PATH, PROJECT_CACHE_SCAFFOLD_PATH

def get_scaffolds_path():
    return SCAFFOLDS_FOLDER_PATH

def get_projects_path():
    return MPL_CACHE_PATH + "/mpl/" + "/projects/"

def get_project_cache_scaffold_path():
    return PROJECT_CACHE_SCAFFOLD_PATH