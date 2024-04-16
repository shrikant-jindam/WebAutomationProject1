import configparser

config = configparser.RawConfigParser()
config.read("C:/Users/Admin/PycharmProjects/WebAutomationProject1/Configurations/config.ini")

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common info','base_url')
        return url
    @staticmethod
    def getUsername():
        username = config.get('common info','username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info','password')
        return password