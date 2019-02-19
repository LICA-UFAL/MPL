import click 
from mpl.utils.custom.click_types import Choice_file
from mpl.utils.project import create_project, get_scaffolds

@click.command()
@click.option("-c","--config", help = "project default configuration .yml file path",
              type = click.Path())
def startproject(config):
    """ Create machine learning project scaffold """
    if not config:
        project_scaffolds_paths = get_scaffolds()
        
        project_name = click.prompt("Project name", default= "My First project")
        project_language = click.prompt("Language", default= "English")
        author_name = click.prompt("Author name")
        author_email = click.prompt("Author email")

        project_scaffold_config = click.prompt("Scaffold type", type = Choice_file(project_scaffolds_paths,
                                             description = "Scaffold config file path"))

        open(project_scaffold_config, "r")
    else:
        create_project(config)


