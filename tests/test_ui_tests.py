import pytest
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.ui_test.jobpage import JobPage
from pageObjects.ui_test.sectorpage import SectorPage
from pageObjects.ui_test.applypage import ApplyPage


class Test_jobs:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    job_page_title = ReadConfig.getvaluesfrom_json('job_page', 'title')
    top_navigation_list = ReadConfig.getkeysfrom_json('navigation_bar_items')
    nav_bar_headers = ReadConfig.getkeysfrom_json('navigation_bar_headers')
    search_bar_list = ReadConfig.getkeysfrom_json('search_bar')
    sector_list = ReadConfig.getkeysfrom_json('sector_list')
    sign_c_links = ReadConfig.getkeysfrom_json('other_link')
    sign_create_headers = ReadConfig.getkeysfrom_json('other_headers')
    lst_apply_job_banking = ReadConfig.getvaluesfrom_json('apply_job', 'Sector_1')
    lst_apply_job_bussiness = ReadConfig.getvaluesfrom_json('apply_job', 'Sector_2')
    search_criteria = "Sector"
    pstr_top_nav = "top_nav"
    pstr_sec_list = "sector_list"
    pstr_search_box = "search_fields_list"

    @pytest.fixture()
    def launch_app(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.jp = JobPage(self.driver)
        assert self.jp.verify_job_page(self.job_page_title)

    @pytest.mark.ui
    def test_page_elements(self, launch_app):
        """  Description:
                |  This method will test page renderng elements
        """
        self.navigation_bar()
        self.search_fields()
        self.sector_list_test()

    @pytest.mark.ui
    def test_top_links(self, launch_app):
        """  Description:
                        |  This method will test link redirections and page headers of top nav, sign and create an account
                """
        self.top_navigation_links()
        self.driver.get(self.baseURL)
        assert self.jp.verify_job_page(self.job_page_title)
        self.sign_create_links()

    @pytest.mark.ui
    def test_apply_jobs(self, launch_app):
        """  Description:
                                |  This method will test end to end scenario of verifying apply job of a specific sector
                                | I have verified pages of Banking sector and Business services sector
                                | You can add sectors in TestData.json and call them here to test it
                        """
        self.apply_job(self.lst_apply_job_banking)
        self.driver.get(self.baseURL)
        assert self.jp.verify_job_page(self.job_page_title)
        self.apply_job(self.lst_apply_job_bussiness)




    def apply_job(self,pstr_sector_name):
        self.logger.info("****Started Apply Job Test****"+pstr_sector_name)
        self.jp.click_sector(pstr_sector_name)
        self.sp = SectorPage(self.driver)
        assert self.sp.verify_sector_page(pstr_sector_name)
        assert self.sp.verify_search_criteria(self.search_criteria, pstr_sector_name)
        assert self.sp.verify_and_click_job()
        self.ap = ApplyPage(self.driver)
        bln_apply = self.ap.verify_job_and_apply('Apply')
        if bln_apply:
            self.logger.info("****Apply Job Successful**" + pstr_sector_name)
            self.logger.info("****Apply Job  Ended ****"  + pstr_sector_name)
        else:
            self.logger.info("****Apply Job unsuccessful****"  + pstr_sector_name)
            self.logger.info("****Apply Job  Ended****" + pstr_sector_name )

    def top_navigation_links(self):
        self.logger.info("****Started Top Navigation link Test****")
        bln_sector = self.jp.verify_top_links(self.top_navigation_list, self.nav_bar_headers)
        if bln_sector:
            self.logger.info("****Top Navigation link Successful****")
            self.logger.info("****Top Navigation link  Ended****")
        else:
            self.logger.info("****Top Navigation link unsuccessful****")
            self.logger.info("****Top Navigation link  Ended****")

    def sign_create_links(self):
        self.logger.info("****Started Sign Create link Test****")
        bln_sector = self.jp.verify_top_links(self.sign_c_links, self.sign_create_headers)
        if bln_sector:
            self.logger.info("****Sign Create link Successful****")
            self.logger.info("****Sign Create link  Ended****")
        else:
            self.logger.info("****Sign Create link unsuccessful****")
            self.logger.info("****Sign Create link  Ended****")

    def navigation_bar(self):
        self.logger.info("****Started Navigation Verification Test****")
        bln_nav = self.jp.verify_list_elements(self.top_navigation_list, self.pstr_top_nav)
        if bln_nav:
            self.logger.info("****Navigation verification test Successful****")
            self.logger.info("****Navigation verification test  Ended****")
        else:
            self.logger.info("****Navigation verification test unsuccessful****")
            self.logger.info("****Navigation verification test  Ended****")

    def search_fields(self):
        self.logger.info("****Started Search field Test****")
        bln_search = self.jp.verify_list_elements(self.search_bar_list, self.pstr_search_box)
        if bln_search:
            self.logger.info("****Search field test Successful****")
            self.logger.info("****Search field test  Ended****")
        else:
            self.logger.info("****Search field test unsuccessful****")
            self.logger.info("****Search field test  Ended****")

    def sector_list_test(self):
        self.logger.info("****Started Sector List Test****")
        bln_sector = self.jp.verify_list_elements(self.sector_list, self.pstr_sec_list)
        if bln_sector:
            self.logger.info("****Sector list test Successful****")
            self.logger.info("****Sector list test  Ended****")
        else:
            self.logger.info("****Sector test unsuccessful****")
            self.logger.info("****Sector test  Ended****")
