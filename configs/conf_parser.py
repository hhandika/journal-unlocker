from configparser import SafeConfigParser

def get_lib_address():
    parser = SafeConfigParser()
    parser.read('configs/settings.conf')
    return parser.get('Settings', 'libs')