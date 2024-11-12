from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        toml_str = request.urlopen(self._url).read().decode("utf-8")
        content = toml.loads(toml_str)
        #print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        tool = content['tool']['poetry']
        return Project(tool)
