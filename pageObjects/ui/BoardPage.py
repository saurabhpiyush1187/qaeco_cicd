from testdata.page_properties.login_locators import Loginlocators
from utilities.customLogger import LogGen
from testdata.page_properties.homepage_locators import Homepagelocators
from testdata.page_properties.createboard_locators import Boardlocators
import os
from utilities.readProperties import ReadConfig
from core.ui.ui_helper import UIHelper

class BoardPage:
    # Board Page
    login_locators = Loginlocators()
    homepage_locators = Homepagelocators()
    board_locators = Boardlocators
    logger = LogGen.loggen()
    explicit_wait = ReadConfig.getexplicitwait()

    def __init__(self,driver):
        self.driver=driver
        self.ui_helper = UIHelper(self.driver)



    def go_to_create_board(self):
        bln_createboard_link = self.ui_helper.is_element_displayed(self.homepage_locators.pstr_createboard_link)
        if bln_createboard_link:
            self.ui_helper.click(self.homepage_locators.pstr_createboard_link)
            self.logger.info("****Create Board link clicked****")
            assert True
        else:
            self.logger.info("****Create Board link Not present or clickable****")
            self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_login_createBoard_link.png")
            self.driver.quit()
            assert False


    def verify_page_header(self,str_pageheader):
        pstr_page_header = self.board_locators.pstr_page_header.format(str_pageheader)
        bln_page_header = self.ui_helper.is_element_displayed(pstr_page_header)
        if bln_page_header:
            self.logger.info("****Page Header is Create a Board****")
            return True
        else:
            self.logger.info("****Page header is different****")
            self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_login_createBoard_header.png")
            self.driver.quit()
            return False


    def create_board(self,str_session_name, owner, str_succes_message):
        bln_session_name = self.ui_helper.is_element_displayed(self.board_locators.pstr_input_session_name)
        if bln_session_name:
            self.ui_helper.type(self.board_locators.pstr_input_session_name,str_session_name)
            self.logger.info("****Entered session name****   " + str(str_session_name))
        else:
            self.logger.info("****Unable to enter session name****")
            self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_login_createBoard_session.png")
            self.driver.quit()
            return False

        bln_owner_drop_down = self.ui_helper.is_element_displayed(self.board_locators.pstr_owner_drop_down)
        if bln_owner_drop_down:
            self.ui_helper.select_dropdown_value(self.board_locators.pstr_owner_drop_down,visible_text=owner)
            self.logger.info("****Selected Owner name****   " + str(owner))
        else:
            self.logger.info("****Unable to select session name****")
            self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_login_createBoard_owner.png")
            self.driver.quit()
            return False

        bln_submit_create_board = self.ui_helper.is_element_displayed(self.board_locators.pstr_createboard_button)
        if bln_submit_create_board:
            self.ui_helper.click(self.board_locators.pstr_createboard_button)
            self.logger.info("****Clicked create board button***")
        else:
            self.logger.info("****Unable to click create board button****")
            self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_login_createBoard_button.png")
            self.driver.quit()
            return False

        bln_pop_up= self.ui_helper.is_element_displayed(self.board_locators.pstr_pop_up)
        if bln_pop_up:
            str_text= self.driver.find_element_by_class_name('swal-title').text
            if str_text== str_succes_message:
                self.logger.info("***Success message verified****")
                return True
            else:
                self.logger.info("***Success message not verified****" + "Expected message: " + str_succes_message + "Actual message: " + str_text)
                self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_login_createBoard_message.png")
                self.driver.quit()
                return False


