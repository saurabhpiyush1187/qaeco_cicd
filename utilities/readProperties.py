import configparser
import os
import json

config=configparser.RawConfigParser()
config.read("."+os.sep+"configurations"+os.sep+"config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url


    @staticmethod
    def getexplicitwait():
        explicit_wait = config.get('common info', 'default_explicit_wait')
        return explicit_wait

    @staticmethod
    def getimplicitwait():
        implicit_wait = config.get('common info', 'default_implicit_wait')
        return implicit_wait


    @staticmethod
    def getvaluesfrom_json(pstr_property, pstr_value):
        try:
            json_path = "." + os.sep + "testdata" + os.sep + "TestData.json"
            with open(json_path, 'r') as myfile:
                data = myfile.read()

            # parse file
            obj = json.loads(data)
            return str(obj[pstr_property][pstr_value])
        except Exception as exception_msg:
            print(exception_msg)
            return False

    @staticmethod
    def getkeysfrom_json(pstr_property):
        try:
            json_path = "." + os.sep + "testdata" + os.sep + "TestData.json"
            with open(json_path, 'r') as myfile:
                data = myfile.read()

            # parse file
            obj = json.loads(data)
            return obj[pstr_property]
        except Exception as exception_msg:
            print(exception_msg)
            return False
