import os
from configparser import SafeConfigParser

from configs import conf_writer

def get_root_dir():
    return os.path.dirname(os.path.abspath(__file__))

def read_settings():
    CONF_DIR = get_root_dir()
    return CONF_DIR + '/' + 'settings.conf'

def read_lib_url():
    parser = SafeConfigParser()
    parser.read(read_settings())
    return parser.get('Settings', 'libs')

def write_user_input(conf):
    conf_write = conf_writer.ConfigWriter(conf)
    conf_write.write_settings()

def get_lib_url():
    try:
        lib_url = read_lib_url()
        return lib_url
    except:
        print('Cannot find a config file')
        print('Add config file')
        conf = input("Enter library address:")
        write_user_input(conf)
        exit()