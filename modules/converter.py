import sys

class LinkConverter:
    def __init__(self, url, libs):
        self.url = url
        self.libs = libs
    
    def _convert_com(self):
        split_url = self.url.split('.com')
        first_part, second_part = split_url
        first_part = first_part.replace('.','-')
        final_link = first_part + '-com.' + self.libs + second_part
        return final_link
    
    def _convert_org(self):
        split_url = self.url.split('.org')
        first_part, second_part = split_url
        first_part = first_part.replace('.','-')
        final_link = first_part + '-org.' + self.libs + second_part
        return final_link

    def _convert_edu(self):
        split_url = self.url.split('.edu')
        first_part, second_part = split_url
        first_part = first_part.replace('.','-')
        final_link = first_part + '-edu.' + self.libs + second_part
        return final_link

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