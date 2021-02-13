import pytest
import os
from pageObjects.LoginPage import LoginPage
from pageObjects.BoardPage import BoardPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from core.ui.ui_helper import UIHelper


class Test_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger=LogGen.loggen()
    create_boardURL = ReadConfig.getvaluesfrom_json('page_urls','create_board')
    create_board_title = ReadConfig.getvaluesfrom_json('title','create_board')
    str_page_header = ReadConfig.getvaluesfrom_json('header', 'create_board')
    session_name = ReadConfig.getvaluesfrom_json('create-board_data', 'session_name')
    owner= ReadConfig.getvaluesfrom_json('create-board_data', 'owner')
    success_message = ReadConfig.getvaluesfrom_json('create-board_data', 'success_message')



    @pytest.mark.smoke
    @pytest.mark.ui
    def test_login_create_board(self,setup):
        try:
            self.logger.info("****Started Login Test****")
            self.driver = setup
            self.driver.maximize_window()
            self.driver.get(self.baseURL)
            self.lp=LoginPage(self.driver)
            self.bp=BoardPage(self.driver)
            assert self.lp.login(self.username,self.password)
            self.bp.go_to_create_board()
            self.ui_helper= UIHelper(self.driver)
            pstr_url = self.driver.current_url
            assert self.ui_helper.verify_url(self.create_boardURL,pstr_url)
            pstr_title = self.driver.title
            assert self.create_board_title,pstr_title
            assert self.bp.verify_page_header(self.str_page_header)
            bln_final_result = self.bp.create_board(self.session_name,self.owner,self.success_message)
            if bln_final_result:
                self.logger.info("*** Test 001 passed****")
                self.driver.close()
                assert True
            else:
                self.logger.error("****Test 001 failed****")
                self.driver.close()
                assert False
        except Exception as exception_msg:
            self.logger.info(exception_msg)
            self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_login_createBoard_exception.png")
            self.driver.close()
            assert False








