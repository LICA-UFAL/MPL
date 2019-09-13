import os

from mpl.utils.scaffold import Scaffold 
from mpl.utils.project.paths import get_scaffolds_path, \
        get_projects_path, get_project_cache_scaffold_path


def create_project(project_name, project_language, author_name, author_email,
                           scaffold_path = None, project_path = os.getcwd(), **extra_config):
    if scaffold_path is not None:
        Scaffold.load_from_file(scaffold_path).run(project_path)

    default_project_cache_scaffold = Scaffold.load_from_file(get_project_cache_scaffold_path())
    dict_project_scaffold = {
        "JsonFile" : ["config.json", {
            "project name" : project_name,
            "project laguage" : project_language,
            "autor_name" : author_name,
            "autor_email" : author_email,
            "project_path" : project_path,
            "extra_config" : extra_config
        }]
    }
    
    default_project_cache_scaffold.update_file_tree(project_name, dict_project_scaffold)
    default_project_cache_scaffold.run(get_projects_path())
    

def get_scaffolds():
    """ Return an list of project scaffold paths """
    return Scaffold.load_scaffolds_from_folder(get_scaffolds_path())
