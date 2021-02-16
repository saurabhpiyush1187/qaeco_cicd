import yaml
from functools import reduce
import operator
import time
import os

class ConfigUtils(object):
    """
    Description:
        |  1. This class contains methods related to fetching data from config_api.yml
        |  2. This class also contains methods to fetch base URLs, default user details, service descriptions and db configurations

    .. note::
        |  Create an object for this class as obj = ConfigUtils(os.getcwd())

    """

    def __init__(self, pstr_current_path):
        """
        Description:
            |  This method is acts as a constructor

        :param pstr_current_path: pass this as os.getcwd()
        :type pstr_current_path: String
        :param pstr_team_config_filename:
        :type pstr_team_config_filename: String

        :return: None
        """
        self.current_path = pstr_current_path
        self.pageobject_dir_path = self.get_pageobjects_dirpath() + os.path.sep + "api"
        self.base_config = self.read_base_config_file()


    def get_config_filepath(self):
        """
        Description:
            |  This method fetches path of config_api.yml

        :return: String
        """
        str_filepath = "."+ os.path.sep + "configurations" + os.path.sep + "config_api.yml"
        return str_filepath

    def read_base_config_file(self):
        """
        Description:
            |  This method reads base config_api.yml file and loads the content into a dictionary object.

        :return: Dictionary
        """

        count = 0
        config = None
        while config is None and count < 30:
            with open(self.get_config_filepath(), 'r') as config_yml:
                config = yaml.load(config_yml)
            count = count + 1
            time.sleep(1)
        if config is None:
            raise Exception("Error Occurred while reading a config file")
        return config



    def get_pageobjects_dirpath(self):
        """
        Description:
            |  This method fetches path of the pageObjects directory

        :return: String
        """
        str_currentdir_path = self.current_path
        str_currentdir_name = os.path.basename(str_currentdir_path)
        while not str_currentdir_name == "pageObjects":
            if os.sep + "pageObjects" in str_currentdir_path:
                str_currentdir_path = os.path.dirname(os.path.abspath(str_currentdir_path))
                str_currentdir_name = os.path.basename(str_currentdir_path)

            else:
                str_currentdir_path = os.path.abspath(str_currentdir_path) + os.sep + "pageObjects"
                str_currentdir_name = os.path.basename(str_currentdir_path)

        return str_currentdir_path




    def get_valuefromyaml_keypath(self, pstr_yaml_filepath, pstr_keypath, pstr_delimiter='/'):
        """
        Description:
            |  This method fetches value of a key from a yaml file

        :param pstr_yaml_filepath:
        :type pstr_yaml_filepath: String
        :param pstr_keypath:
        :type pstr_keypath: String

        :return: List
        Examples:
            |  An example of pstr_keypath is root/level1/level2/key

        """
        with open(pstr_yaml_filepath, 'r') as config_yml:
            config = yaml.load(config_yml)
        lst_key = pstr_keypath.split(pstr_delimiter)
        return reduce(operator.getitem, lst_key, config)

    def get_valuefrom_configobject(self, pobj_config, pstr_keypath, pstr_delimiter='/'):
        """
        Description:
            |  This method fetches value of a key from a yaml file

        :param pobj_config:
        :type pobj_config: Dictionary
        :param pstr_keypath:
        :type pstr_keypath: String

        :return: List
        Examples:
            |  An example of pstr_keypath is root/level1/level2/key

        """
        lst_key = pstr_keypath.split(pstr_delimiter)
        return reduce(operator.getitem, lst_key, pobj_config)


    def fetch_base_url(self):
        """
        Description:
            |  This method fetches base_url for the environment selected based on the values applied for the keys execution_environment and environment_type in the config_api.yml

        :return: String
        """
        str_execution_environment = self.fetch_execution_environment()
        str_environment_type = self.fetch_environment_type()
        str_base_url = self.base_config["env"][str_execution_environment][str_environment_type]["base_url"]
        return str_base_url

    def fetch_environment_type(self):
        """
        Description:
            |  This method fetches the environment type from config_api.yml

        :return: String
        """
        return self.base_config.get("environment_type")

    def fetch_execution_environment(self):
        """
        Description:
            |  This method fetches the execution environment from config_api.yml

        :return: String
        """
        return self.base_config.get("execution_environment")


    def fetch_servicedescription_path(self):
        """
        Description:
            |  This method fetches path of the pageObjects/api/service_description directory

        :return: String
        """
        str_service_description_path = self.base_config["service_description"]
        str_service_description_path = os.path.join(self.pageobject_dir_path, str_service_description_path)
        return str_service_description_path

    def fetch_servicepayload_path(self):
        """
        Description:
            |  This method fetches path of the pageObjects/api/services/payloads directory

        :return: String
        """
        str_service_payloads_path = self.base_config["service_payloads"]
        str_service_payloads_path = os.path.join(self.pageobject_dir_path, str_service_payloads_path)
        return str_service_payloads_path



    def fetch_login_credentials(self, pstr_user_account_type="default_user"):
        """
        Description:
            |  By default, this method returns username and password of 'default_user' mentioned in config_api.yml. If pstr_user_account_type is not 'default_user' then it returns username and password of the user_type mentioned in team_config.yml

        :param pstr_user_account_type: Default value is 'default_user'
        :type pstr_user_account_type: String

        :return: List [str_username, str_password]
        """
        str_username =''
        str_password=''
        str_execution_environment = self.fetch_execution_environment()
        str_environment_type = self.fetch_environment_type()
        if pstr_user_account_type == "default_user":
            str_username = \
            self.base_config["env"][str_execution_environment][str_environment_type][pstr_user_account_type][
                "username"]
            str_password = \
            self.base_config["env"][str_execution_environment][str_environment_type][pstr_user_account_type][
                "password"]

        return str_username, str_password

    def get_servicedescription(self, pstr_service_desc_relfilepath, pstr_keypath):
        """
        Description:
            |  This method fetches entire service description of a particular service mentioned in service description yaml file.
            |  The service description yaml file contains below keys
            |  method:
            |  endpoint:
            |  queryparams:
            |  headers:
            |  payload:
            |  target_url:

        :param pstr_service_desc_relfilepath: Relative path of the service description file
        :type pstr_service_desc_relfilepath: String
        :param pstr_keypath:
        :type pstr_keypath: String

        :return: Dictionary
        .. code-block:: python

            Sample service description appears as

            entity_search:
                method: GET
                endpoint: "/.Services.Search.Service/v2/typeahead/query"
                queryparams: "?start=0&rows=15&SearchToken=Down2Earth II&Catalogs=funds&RequestType=2"
                headers: {'Authorization': 'Bearer', 'Content-Type':'application/json'}
                payload: None
                target_url: target_url_1

        """
        dict_service_desc = {}
        str_service_desc_path = os.path.join(self.fetch_servicedescription_path(), pstr_service_desc_relfilepath)
        dict_service_description = self.get_valuefromyaml_keypath(str_service_desc_path, pstr_keypath)

        dict_service_desc["target_url"] = self.fetch_base_url()


        dict_service_desc["method"] = dict_service_description.get("method")
        dict_service_desc["endpoint"] = dict_service_description.get("endpoint")
        if dict_service_description.get("queryparams") == "None":
            dict_service_desc["queryparams"] = ""
        else:
            dict_service_desc["queryparams"] = dict_service_description.get("queryparams")
        if dict_service_description.get("headers") == "None":
            dict_service_desc["headers"] = {}
        else:
            dict_service_desc["headers"] = dict_service_description.get("headers")
        dict_service_desc["payload"] = dict_service_description.get("payload", "None")
        if not dict_service_desc["payload"] == "None":
            str_payload_path = os.path.join(self.fetch_servicepayload_path(), dict_service_desc["payload"])
            with open(str_payload_path, 'r') as file:
                str_file_data = file.read()
                dict_service_desc["payload"] = str_file_data
        return dict_service_desc



