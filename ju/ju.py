
import click
import configparser

from configs import conf_parser
from modules import input_output

@click.command()
@click.option('--url','-u', help='Add a url, doi link, or doi name.')
def main(url):
    """[summary]

    Args:
        url (text): Add url from the journal list.

    Returns:
        [type]: [description]
    """
    libs = conf_parser.get_lib_address()
    ui = input_output.UserInput(libs, url)
    ui.check_user_input()