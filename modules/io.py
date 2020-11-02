import webbrowser as wb
from modules import converter as cv

class UserInput:
    def __init__(self, libs, url):
        self.libs = libs
        self.url = url

    def _convert_doi(self):
        doi = 'https://doi.org/'
        link = doi + self.url
        access_link = cv.convert_url(link, self.libs)
        wb.open(access_link)

    def _convert_http(self):
        access_link = cv.convert_url(self.url, self.libs)
        wb.open(access_link)
    
    def _convert_url(self):
        if self.url.startswith('10'):
            self._convert_doi()
        elif self.url.startswith('http'):
            self._convert_http()
        else:
            print("ERROR: Invalid URL")
            print("Please, enter a valid url or doi name.")
            print("The url should start with 'http'")
            print("if it is a doi name, the prefix should start with '10.'")
        
    def _is_empty_input(self):
        self.url = input("Enter url/doi:")
        self._convert_url()

    def check_user_input(self):
        if self.url is None:
            self._is_empty_input()
        else:
            self._convert_url()