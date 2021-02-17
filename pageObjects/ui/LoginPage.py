from testdata.page_properties.login_locators import Loginlocators
from utilities.customLogger import LogGen
from testdata.page_properties.homepage_locators import Homepagelocators
from testdata.page_properties.createboard_locators import Boardlocators
import os
from core.ui.ui_helper import UIHelper

class LoginPage:
    # Login Page
    login_locators = Loginlocators()
    homepage_locators = Homepagelocators()
    board_locators = Boardlocators
    logger = LogGen.loggen()

    def __init__(self,driver):
        self.driver=driver
        self.ui_helper = UIHelper(self.driver)


    def setUserName(self, username):
            bln_email = self.ui_helper.is_element_displayed(self.login_locators.pstr_email_address)
            if bln_email:
                self.logger.info("****Entering Email address****")
                self.ui_helper.type(self.login_locators.pstr_email_address,username)
                self.logger.info("****Entered Email address***  " + username)
                assert True
            else:
                self.logger.info("****Email address box not present****")
                self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_setusername.png")
                self.driver.close()
                assert False


    def setPassword(self, password):
        bln_password = self.ui_helper.is_element_displayed(self.login_locators.pstr_password)
        if bln_password:
            self.logger.info("****Entering password****")
            self.ui_helper.type(self.login_locators.pstr_password,password)
            self.logger.info("****Entered Password****  " + password)
            assert True
        else:
            self.logger.info("****Password box not present****")
            self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_setpassword.png")
            self.driver.close()
            assert False

    def clickLogin(self):
        bln_submit = self.ui_helper.is_element_displayed(self.login_locators.pstr_submit_button)
        if bln_submit:
            self.logger.info("****Clicking Submit button****")
            self.ui_helper.click(self.login_locators.pstr_submit_button)
            self.logger.info("****Submit button clicked****")
            assert True
        else:
            self.logger.info("****Submit Button not present****")
            self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_login_submit.png")
            self.driver.close()
            assert False

    def verify_loginpage(self):
        bln_result = False
        self.logger.info("****Verifying Login page****")
        bln_sprintboard = self.ui_helper.is_element_displayed(self.login_locators.pstr_verify_login_page)
        bln_email = self.ui_helper.is_element_displayed(self.login_locators.pstr_email_address)
        if bln_sprintboard and bln_email:
            bln_result= True
            self.logger.info("****User is on the login page****")
        else:
            self.logger.info("****User is not on the login page****")
            self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_loginpage.png")
            self.driver.close()
        return bln_result

    def verify_homepage(self):
        self.logger.info("****Verifying Home page****")
        bln_homepage = self.ui_helper.is_element_displayed(self.homepage_locators.pstr_verify_home_page)
        if bln_homepage:
            bln_homepage = True
            self.logger.info("****User is on the home page****")
        else:
            self.logger.info("****User is not on the home page****")
            self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_homepage.png")
            self.driver.close()
        return bln_homepage


    def login(self,username,password):
        assert self.verify_loginpage()
        self.setUserName(username)
        self.setPassword(password)
        self.clickLogin()
        bln_homepage= self.verify_homepage()
        return bln_homepage




