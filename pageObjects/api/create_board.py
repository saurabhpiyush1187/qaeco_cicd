import os
import json
from utilities.config_utils import ConfigUtils
from core.api.api_helper import RequestBuilder
from pageObjects.api.common_utils import CommonUtils
from utilities.customLogger import LogGen



class CreateBoard:
    config_utils = ConfigUtils(os.getcwd())
    request_builder = RequestBuilder()
    mi_common_utils = CommonUtils()
    logger = LogGen.loggen()

    def __init__(self):
        self.response = ""
        self.response_content= ""
        self.str_request_url = ""
        self.uuid=""
        self.str_auth_token =""


    def validate_reponse(self):
        """
        Description:
        	|  This method calls the is_responsevalid from comon_utils to validate the response code
        :return: None
        """
        bln_response = self.mi_common_utils.is_responsevalid(self.response)
        return bln_response


    def create_board(self):
        self.str_auth_token = self.mi_common_utils.springboard_get_authtoken()
        dict_service_disc = self.config_utils.get_servicedescription("springboard_description.yml", "create_board")
        str_request_url = dict_service_disc["target_url"] + dict_service_disc["endpoint"] + dict_service_disc[
            "queryparams"]
        headers = dict_service_disc["headers"]
        headers["Authorization"] = "Bearer "+self.str_auth_token
        payload = dict_service_disc["payload"]
        self.response = self.request_builder.call_request(dict_service_disc["method"], str_request_url,
                                                       headers, pstr_payload=payload)
        self.response_content = self.response.content
        bln_response1 = self.mi_common_utils.is_reponsegenerated(self.response)
        bln_validate_response = self.validate_reponse()
        response_json = json.loads(self.response_content)
        if bln_response1 and bln_validate_response:
            self.logger.info("*****Board is created successfully***")
            self.uuid = response_json['data']['uuid']
            return self.uuid,self.str_auth_token
        else:
            self.logger.info("*****Board is not created successfully***Response code"+ str(self.response.status_code) )
            return None


    def verify_created_board(self,uuid):
        dict_service_disc = self.config_utils.get_servicedescription("springboard_description.yml", "get_board")
        str_request_url = dict_service_disc["target_url"] + dict_service_disc["endpoint"] +"/"+ str(uuid)+ dict_service_disc[
            "queryparams"]
        headers = dict_service_disc["headers"]
        headers["Authorization"] = "Bearer "+self.str_auth_token
        payload = dict_service_disc["payload"]
        self.response = self.request_builder.call_request(dict_service_disc["method"], str_request_url,
                                                       headers, pstr_payload=payload)
        self.response_content = self.response.content
        bln_response1 = self.mi_common_utils.is_reponsegenerated(self.response)
        bln_validate_response = self.validate_reponse()
        response_json = json.loads(self.response_content)
        if bln_response1 and bln_validate_response:
            pstr_uuid = response_json['data']['uuid']
            if pstr_uuid == uuid:
                self.logger.info("*****Board is verified successfully***")
                return True
        else:
            self.logger.info("*****Board is not verified successfully***Response code"+ str(self.response.status_code) )
            return False




