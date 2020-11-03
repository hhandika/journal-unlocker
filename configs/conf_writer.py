import os

class ConfigWriter:
    def __init__(self, lib_url):
        self.lib_url = lib_url
    
    def _get_root_path(self):
        return os.path.dirname(os.path.abspath(__file__))

    def _get_settings(self):
        ROOT_DIR = self._get_root_path()
        fname = ROOT_DIR + '/' + 'settings.conf'
        url = 'libs = ' + self.lib_url
        return fname, url

    def write_settings(self):
        fname, url = self._get_settings()
        f = open(fname, 'a')
        f.write('[Settings]\n')
        f.write(url)
        f.close()
        print('You are set!')
        print(f"A config file is written in {fname}\n")