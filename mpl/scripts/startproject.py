import click 

from mpl.utils.file import read_file_to_dict 
from mpl.utils.custom.click_types import ChoiceElement
from mpl.utils.project import create_project, get_scaffolds



@click.command()
@click.option("-c","--config", help = "project default configuration .yml file path",
              type = click.Path())
def startproject(config):
    """ Create machine learning project scaffold """
    if not config:
        project_scaffolds = get_scaffolds()
        
        project_name = click.prompt("Project name", default= "My First project")
        project_language = click.prompt("Language", default= "English")
        author_name = click.prompt("Author name")
        author_email = click.prompt("Author email")

        project_scaffold = click.prompt("Scaffold type", type = ChoiceElement(project_scaffolds,
                                             description = "Scaffold config file path"))


        create_project(project_name, project_language, author_name,
                        author_email, scaffold = project_scaffold)
    else:
        dict_config = read_file_to_dict(config)
        create_project(**dict_config)


