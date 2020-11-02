
import click

from modules import user_input

@click.command()
@click.option('--url','-u', help='Add a url, doi link, or doi name.')
def main(url):
    """[summary]

    Args:
        url (text): Add url from the journal list.

    Returns:
        [type]: [description]
    """
    libs = 'libezp.lib.lsu.edu'
    ui = user_input.UserInput(libs, url)
    ui.check_user_input()
        