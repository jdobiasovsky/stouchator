import json


class ConfigurationProperties:
    def __init__(self):
        with open('config.json', 'r') as configfile:
            config = json.load(configfile)
        self.inputdir = config['paths']['inputdir']
        self.outputdir = config['paths']['outputdir']
        self.ocrinput = config['paths']['ocrinput']
        self.ocroutput = config['paths']['ocroutput']

    def getinputdir(self):
        return self.inputdir

    def getoutputdir(self):
        return self.outputdir

    def getocrinput(self):
        return self.ocrinput

    def getocroutput(self):
        return self.ocroutput
