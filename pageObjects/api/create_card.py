import os
import json
from utilities.config_utils import ConfigUtils
from core.api.api_helper import RequestBuilder
from pageObjects.api.common_utils import CommonUtils
from utilities.customLogger import LogGen



class Createcard:
    config_utils = ConfigUtils(os.getcwd())
    request_builder = RequestBuilder()
    mi_common_utils = CommonUtils()
    logger = LogGen.loggen()

    def __init__(self):
        self.response = ""
        self.response_content= ""
        self.str_request_url = ""
        self.str_auth_token =""


    def validate_reponse(self):
        """
        Description:
        	|  This method calls the is_responsevalid from comon_utils to validate the response code
        :return: None
        """
        bln_response = self.mi_common_utils.is_responsevalid(self.response)
        return bln_response


    def get_card_column_uuid(self,board_uuid, str_token, pstr_card_type):
        self.str_auth_token = str_token
        dict_service_disc = self.config_utils.get_servicedescription("springboard_description.yml", "get_board")
        str_request_url = dict_service_disc["target_url"] + dict_service_disc["endpoint"] +"/"+ str(board_uuid)+ dict_service_disc[
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
            for i in range(0,3):
                if response_json['data']['columns'][i]['title']==pstr_card_type:
                    self.logger.info("*****Card Column found***")
                    str_uuid= response_json['data']['columns'][i]['uuid']
                    return str_uuid
            else:
                self.logger.info("*****Card Column not found***")
                return None
        else:
            self.logger.info("*****Board is not verified successfully***Response code"+ str(self.response.status_code) )
            return None


    def create_card(self,str_card_column_uuid, str_token,card_type):
        dict_service_disc={}
        self.str_auth_token = str_token
        if card_type=="Went well":
            dict_service_disc = self.config_utils.get_servicedescription("springboard_description.yml", "create_well_card")
        elif card_type=="Didn't go well":
            dict_service_disc = self.config_utils.get_servicedescription("springboard_description.yml","create_not_well_card")
        str_request_url = dict_service_disc["target_url"] + dict_service_disc["endpoint"] + dict_service_disc["queryparams"]
        headers = dict_service_disc["headers"]
        headers["Authorization"] = "Bearer " + self.str_auth_token
        payload = dict_service_disc["payload"] +"," + "\"" + "column_uuid" + "\"" + ":" + "\"" + str_card_column_uuid + "\"" +"}"
        self.response = self.request_builder.call_request(dict_service_disc["method"], str_request_url,
                                                          headers, pstr_payload=payload)
        self.response_content = self.response.content
        bln_response1 = self.mi_common_utils.is_reponsegenerated(self.response)
        bln_validate_response = self.validate_reponse()
        response_json = json.loads(self.response_content)
        if bln_response1 and bln_validate_response:
            self.logger.info("*****Card is created successfully***")
            card_uuid = response_json['data']['uuid']
            return card_uuid
        else:
            self.logger.info("*****Card is not created successfully***Response code"+ str(self.response.status_code) )
            return None



    def like_card(self,str_card_uuid, str_token):
        self.str_auth_token = str_token
        dict_service_disc = self.config_utils.get_servicedescription("springboard_description.yml", "like_card")
        str_request_url = dict_service_disc["target_url"] + dict_service_disc["endpoint"] +"/"+ str(str_card_uuid)+"/like"+ dict_service_disc["queryparams"]
        headers = dict_service_disc["headers"]
        headers["Authorization"] = "Bearer " + self.str_auth_token
        payload = dict_service_disc["payload"]
        self.response = self.request_builder.call_request(dict_service_disc["method"], str_request_url,
                                                          headers, pstr_payload=payload)
        self.response_content = self.response.content
        bln_response1 = self.mi_common_utils.is_reponsegenerated(self.response)
        bln_validate_response = self.validate_reponse()
        response_json = json.loads(self.response_content)
        if bln_response1 and bln_validate_response:
            self.logger.info("*****Like request send successfully***")
            status = response_json['status']
            return status
        else:
            self.logger.info("*****Like request unsuccessfull***Response code"+ str(self.response.status_code) )
            return None


    def delete_card(self,str_card_uuid, str_token):
        self.str_auth_token = str_token
        dict_service_disc = self.config_utils.get_servicedescription("springboard_description.yml", "delete_card")
        str_request_url = dict_service_disc["target_url"] + dict_service_disc["endpoint"] +"/"+ str(str_card_uuid)+ dict_service_disc["queryparams"]
        headers = dict_service_disc["headers"]
        headers["Authorization"] = "Bearer " + self.str_auth_token
        payload = dict_service_disc["payload"]
        self.response = self.request_builder.call_request(dict_service_disc["method"], str_request_url,
                                                          headers, pstr_payload=payload)
        self.response_content = self.response.content
        bln_response1 = self.mi_common_utils.is_reponsegenerated(self.response)
        bln_validate_response = self.validate_reponse()
        response_json = json.loads(self.response_content)
        if bln_response1 and bln_validate_response:
            self.logger.info("*****Delete request send successfully***")
            status = response_json['status']
            return status
        else:
            self.logger.info("*****Delete request unsuccessfull***Response code"+ str(self.response.status_code) )
            return None



