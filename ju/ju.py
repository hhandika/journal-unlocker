import click

from configs import conf_reader
from configs import conf_writer
from modules import input_output


def show_version():
    version = "v0.0.1"
    print(f"Journal Unlocker {version}")

@click.command()
@click.option('--url','-u', help='Add a url, doi link, or doi name.')
@click.option('--set', default=None, help='Set library url.')
@click.option('--version', default=None, is_flag=True, help='Show version')
def main(url, set, version):
    """[summary]

    Args:
        url (text): Add url from the journal list.

    Returns:
        [type]: [description]
    """
    if set is not None:
        settings = conf_writer.ConfigWriter(set)
        settings.write_settings()
    elif version is not None:
        show_version()
    else:
        libs = conf_reader.get_lib_url()
        ui = input_output.UserInput(libs, url)
        ui.check_user_input()
