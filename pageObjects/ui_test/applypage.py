from utilities.customLogger import LogGen
import os
from testdata.page_properties.applypage_locators import Applyjobs
from utilities.readProperties import ReadConfig
from core.ui.ui_helper import UIHelper


class ApplyPage:
    # Job Page
    logger = LogGen.loggen()
    explicit_wait = ReadConfig.getexplicitwait()
    apply_locator = Applyjobs()
    baseURL = ReadConfig.getApplicationURL()

    def __init__(self, driver):
        self.driver = driver
        self.ui_helper = UIHelper(self.driver)

    def verify_job_and_apply(self, pstr_button_name):
        """  Description:
                    |  This method will verify job description and apply button
                :param pstr_button_name: Name of the Apply button E.g: Apply, Apply here, Apply Now
                :type pstr_button_name: String

                :return: boolean

                                        """
        bln_job_result = False
        bln_button = False
        pstr_job = self.ui_helper.is_element_displayed(self.apply_locator.pstr_job_desc)
        if pstr_job:
            lst_web_ele = self.driver.find_elements_by_xpath(self.apply_locator.pstr_job_desc.split('=', 1)[1])
            str_job = lst_web_ele[1].text
            if str_job != ' ' or str_job is not None:
                bln_job_result = True
                self.logger.info("****Job description found****")
            else:
                self.logger.info("****Job description not found****")
                self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_job_desc_fail.png")
                self.driver.close()
                return False
        pstr_button = self.apply_locator.pstr_apply_button.format(pstr_button_name)
        web_ele = self.driver.find_elements_by_xpath(pstr_button)
        if web_ele is not None:
            bln_button = True
            self.logger.info("****Apply button found****")
        else:
            self.logger.info("****Apply button found not found****")
            self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_apply_fail.png")
            self.driver.close()
            return False
        return bln_button or bln_job_result
