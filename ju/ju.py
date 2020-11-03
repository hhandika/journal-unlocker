
import click
import configparser

from configs import conf_reader
from configs import conf_writer
from modules import input_output

@click.command()
@click.option('--url','-u', help='Add a url, doi link, or doi name.')
@click.option('--set', default=None, help='Set library url.')
def main(url, set):
    """[summary]

    Args:
        url (text): Add url from the journal list.

    Returns:
        [type]: [description]
    """
    if set is not None:
        write_lib = conf_writer.ConfigWriter(set)
        write_lib.write_settings()
    else:
        libs = conf_reader.get_lib_url()
        ui = input_output.UserInput(libs, url)
        ui.check_user_input()