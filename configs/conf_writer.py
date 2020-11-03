import os

from configs import conf_reader

class ConfigWriter:
    def __init__(self, lib_url):
        self.lib_url = lib_url

    def _get_url(self):
        return 'libs = ' + self.lib_url

    def write_settings(self):
        fname = conf_reader.read_settings()
        url = self._get_url()
        f = open(fname, 'a')
        f.write('[Settings]\n')
        f.write(url)
        f.close()
        print('You are set!')
        print(f"A config file is written in {fname}\n")