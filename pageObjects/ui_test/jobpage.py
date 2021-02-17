from utilities.customLogger import LogGen
from testdata.page_properties.jobpage_locators import Joblocators
import os
from utilities.readProperties import ReadConfig
from core.ui.ui_helper import UIHelper


class JobPage:
    # Job Page
    logger = LogGen.loggen()
    explicit_wait = ReadConfig.getexplicitwait()
    job_locator = Joblocators()
    baseURL = ReadConfig.getApplicationURL()

    def __init__(self, driver):
        self.driver = driver
        self.ui_helper = UIHelper(self.driver)

    def verify_job_page(self, str_pageheader):
        """  Description:
                                |  This method will allow user to verify base page
                                :param str_pageheader: Page header
                                :type str_pageheader: String

                                :return: None

                                                        """
        pstr_page_header = self.job_locator.pstr_verify_home_page.format(str_pageheader)
        bln_page_header = self.ui_helper.is_element_displayed(pstr_page_header)
        if bln_page_header:
            self.logger.info("****User is on the Job page****")
            return True
        else:
            self.logger.info("****User is not on the Job page****")
            self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_login.png")
            self.driver.close()
            return False

    def verify_list_elements(self, pstr_naivigation_list, pstr_list_type):
        """  Description:
            |  This method will verify list_elements rendering on the page
        :param pstr_naivigation_list: list of elements to be verified
        :type pstr_naivigation_list: Dictionary
        :param pstr_list_type: type of list. E.g. Top Nav, sector list,etc.
        :type pstr_list_type: String

        :return: boolean

                                """
        bln_top = False
        pstr_actual_list = []
        if pstr_list_type == "sector_list":
            pstr_nav_list = pstr_naivigation_list.values()
            pstr_web_elem = self.driver.find_elements_by_xpath(self.job_locator.pstr_sector_list)
            bln_top = self.ui_helper.match_attributes_by_text(pstr_nav_list, pstr_web_elem)
        elif pstr_list_type == "top_nav":
            pstr_nav_list = pstr_naivigation_list.keys()
            pstr_web_elem = self.driver.find_elements_by_xpath(self.job_locator.pstr_nav_list)
            bln_top = self.ui_helper.match_attributes_by_text(pstr_nav_list, pstr_web_elem)
        elif pstr_list_type == "search_fields_list":
            pstr_search_placeholders = pstr_naivigation_list.values()
            pstr_web_ele_search = self.driver.find_elements_by_xpath(self.job_locator.pstr_search_list)
            if len(pstr_search_placeholders) == len(pstr_web_ele_search):
                for element in pstr_web_ele_search:
                    pstr_actual_list.append(element.get_attribute("placeholder"))
                bln_top = ', '.join(map(str, pstr_search_placeholders)) in ', '.join(map(str, pstr_actual_list))
            else:
                self.logger.info("****Search box count mismatched. There may be few or more****")
                self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_job_search_fields.png")
                self.driver.close()
                return False

        return bln_top


    def verify_top_links(self, pstr_nav_links, pstr_nav_headers):
        """  Description:
                    |  This method will verify links redirection along with pae headers
                :param pstr_nav_links: list of links to be verified on the page
                :type pstr_nav_links: Dictionary
                :param pstr_nav_headers: list of headers to be verified
                :type pstr_nav_headers: Dictionary

                :return: boolean

                                        """
        bln_verify_link = False
        bln_page_header = False
        for prop, value in pstr_nav_links.items():
            pstr_val = pstr_nav_headers[prop]
            pstr_link = self.job_locator.pstr_nav_links.format(prop)
            bln_pstr_link = self.ui_helper.is_element_displayed(pstr_link)
            if bln_pstr_link:
                self.ui_helper.click(pstr_link)
                pstr_page_header = self.job_locator.pstr_nav_head.format(pstr_val)
                bln_page_header = self.ui_helper.is_element_displayed(pstr_page_header)
                given_link = self.baseURL + value
                pstr_url = self.driver.current_url
                bln_verify_link = self.ui_helper.verify_url(given_link, pstr_url)
            else:
                self.logger.info("**** Link not found. ****")
                self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_job_nav_link.png")
                self.driver.close()
                return False
        if bln_verify_link and bln_page_header:
            self.logger.info("**** Page headers verified ****")
            return True
        else:
            return False

    def click_sector(self, pstr_sector_type):
        """  Description:
                        |  This method will click on the sector type
                        :param pstr_sector_type: Name of type of sector
                        :type pstr_sector_type: String

                        :return: None

                                                """
        pstr_web_elem = self.driver.find_elements_by_xpath(self.job_locator.pstr_sector_list)
        for element in pstr_web_elem:
            if element.text == pstr_sector_type:
                element.click()
                self.logger.info(pstr_sector_type + "**** Clicked****")
                break

            else:
                self.logger.info(pstr_sector_type + "**** Not found****")
