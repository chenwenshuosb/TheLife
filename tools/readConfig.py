import configparser
from config.settings import configDir

class ReadIniFile():

    def __init__(self):
        self.config=configparser.ConfigParser()
        self.read=self.config.read(configDir,encoding='utf-8')

    def readFile(self,section,option):
        return self.config.get(section,option)


