import click
from mpl import __version__
from mpl.scripts import startproject


def version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(__version__)
    ctx.exit()

@click.group()
@click.option('--version', is_flag=True, callback=version,
              expose_value=False, is_eager=True)
def cli():
    """ Welcome to Model processing library """
    pass


cli.add_command(startproject.startproject)