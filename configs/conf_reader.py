from configparser import SafeConfigParser

from configs import conf_writer

def read_lib_url():
    parser = SafeConfigParser()
    parser.read('configs/settings.conf')
    return parser.get('Settings', 'libs')

def write_user_input(conf):
    conf_write = conf_writer.ConfigWriter(conf)
    conf_write.write_settings()

def get_lib_url():
    try:
        lib_url = read_lib_url()
        return lib_url
    except:
        print('Error reading config file')
        print('Add config file')
        conf = input("Enter library address:")
        write_user_input(conf)
        exit()