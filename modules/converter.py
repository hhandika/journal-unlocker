import sys

class LinkConverter:
    def __init__(self, url, libs):
        self.url = url
        self.libs = libs
    
    def _split_url(self, domain):
        split_url = self.url.split(domain)
        first_part, second_part = split_url
        first_part = first_part.replace('.','-')
        domain = domain.replace('.', '-')
        return first_part + domain + '.' + self.libs + second_part
    
    def _convert_com(self):
        domain = '.com'
        return self._split_url(domain)
    
    def _convert_org(self):
        domain = '.org'
        return self._split_url(domain)

    def _convert_edu(self):
        domain = '.edu'
        return self._split_url(domain)

    def convert_url(self):
        if '.com' in self.url:
            url = self._convert_com()
            return url
        elif '.org' in self.url:
            url = self._convert_org()
            return url
        elif '.edu' in self.url:
            url = self._convert_edu()
            return url
        else:
            sys.exit(f'\x1b[0;31mERROR: \x1b[0mTHE URL IS NOT SUPPORTED') 