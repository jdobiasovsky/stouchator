"""Module for reading the config."""
import json


class ConfigurationProperties:
    """Read configuraiton."""

    def __init__(self):
        """Load and read config.json."""
        with open('config.json', 'r') as configfile:
            config = json.load(configfile)
        self.inputdir = config['paths']['inputdir']
        self.outputdir = config['paths']['outputdir']
        self.ocrinput = config['paths']['ocrinput']
        self.ocroutput = config['paths']['ocroutput']

    def getinputdir(self):
        """Provide program input directory."""
        return self.inputdir

    def getoutputdir(self):
        """Provide program output directory."""
        return self.outputdir

    def getocrinput(self):
        """Provide ocr input."""
        return self.ocrinput

    def getocroutput(self):
        """Provide ocr output."""
        return self.ocroutput
