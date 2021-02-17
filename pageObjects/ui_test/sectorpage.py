import os
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from testdata.page_properties.sectorpage_locators import Sectorjobs
from core.ui.ui_helper import UIHelper


class SectorPage:
    # Job Page
    logger = LogGen.loggen()
    explicit_wait = ReadConfig.getexplicitwait()
    sector_locator = Sectorjobs()
    baseURL = ReadConfig.getApplicationURL()

    def __init__(self, driver):
        self.driver = driver
        self.ui_helper = UIHelper(self.driver)

    def verify_sector_page(self, sector_header):
        """  Description:
                    |  This method will verify header of the sector page
                :param sector_header: Name of the sector
                :type sector_header: String

                :return: boolean

                                        """
        sector_header = sector_header + ' jobs'
        pstr_header = self.sector_locator.pstr_sector_head.format(sector_header)
        bln_page_header = self.ui_helper.is_element_displayed(pstr_header)
        if bln_page_header:
            self.logger.info("****User is on the Sector Job page****")
        else:
            self.logger.info("****User is not on the Sector Job page****")
            self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_login_sector_job.png")
            self.driver.close()
        return bln_page_header

    def verify_search_criteria(self, pstr_criteria, sector_header):
        """  Description:
                    |  This method will verify search criteria with respect to sector
                :param pstr_criteria: Search criteria E.g. Sectors
                :type pstr_criteria: String
                :param sector_header: Name of the sector
                :type sector_header: String

                :return: boolean

                                        """
        pstr_header = self.sector_locator.pstr_selected_sector.format(pstr_criteria, sector_header)
        bln_page_header = self.ui_helper.is_element_displayed(pstr_header)
        if bln_page_header:
            self.logger.info("****User is on the Job page****")
        else:
            self.logger.info("****User is not on the Job page****")
            self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_search_sector.png")
            self.driver.close()
        return bln_page_header

    def verify_and_click_job(self):
        """  Description:
                        |  This method will verify available job list and click on the job
                        :return: None

                                                """
        pstr_job = self.ui_helper.is_element_displayed(self.sector_locator.pstr_list_job)
        if pstr_job:
            lst_web_ele = self.driver.find_elements_by_xpath(self.sector_locator.pstr_list_job.split('=', 1)[1])
            if lst_web_ele is not None:
                # clicking on the first job
                lst_web_ele[1].click()
                self.logger.info("****Job list returns****")
                self.logger.info("****Job list is clicked****")
                return True
            else:
                self.logger.info("****Job list not returned****")
                self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_job_list.png")
                self.driver.close()
                return False
        else:
            self.logger.info("****Job list not returned****")
            self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_job_list.png")
            self.driver.close()
            return False
