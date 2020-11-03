from configparser import SafeConfigParser

def read_lib_address():
    parser = SafeConfigParser()
    parser.read('configs/settings.conf')
    return parser.get('Settings', 'libs')