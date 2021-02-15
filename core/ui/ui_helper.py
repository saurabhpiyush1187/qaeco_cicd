from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
import re


class UIHelper():
    # UI Helper class
    logger = LogGen.loggen()
    explicit_wait = float(ReadConfig.getexplicitwait())

    def __init__(self,driver):
        self.driver=driver
        self.locator_strategies = ['XPATH', 'ID', 'NAME', 'CLASS_NAME', 'LINK_TEXT',
                                   'CSS_SELECTOR', 'PARTIAL_LINK_TEXT', 'TAG_NAME']


    def is_element_displayed(self, locator, explicit_wait=None):
        if explicit_wait is None:
            explicit_wait = self.explicit_wait

        if isinstance(locator, str):

            locator_details = locator.split('=', 1)
            element = WebDriverWait(self.driver, explicit_wait).until(
                EC.visibility_of_element_located(
                    (self.get_locator_strategy(locator_details[0]), locator_details[1])))
            if element is not None:
                return True
            else:
                return False
        elif isinstance(locator, WebElement):
            return locator.is_displayed()


    def click(self, locator, explicit_wait=None):
        self.get_clickable_web_element(locator, explicit_wait).click()


    def get_clickable_web_element(self, locator, explicit_wait=None):
        if explicit_wait is None:
            explicit_wait = self.explicit_wait

        if isinstance(locator, str):
            locator_details = locator.split('=', 1)

            return WebDriverWait(self.driver, explicit_wait).until(
                EC.element_to_be_clickable((self.get_locator_strategy(locator_details[0]), locator_details[1])))



    def type(self, locator, text, pbool_clear=False, explicit_wait=None, pbool_click_before_type=True):
        if pbool_click_before_type:
            self.get_clickable_web_element(locator, explicit_wait).click()
        if pbool_clear:
            self.get_clickable_web_element(locator, explicit_wait).clear()
        self.get_clickable_web_element(locator, explicit_wait).send_keys(text)

    def get_locator_strategy(self, pstr_locator_strategy):
        """
        Description:
            |  this method returns the type of the locator, if pstr_locator_strategy is not in given strategies it returns an error

        :param pstr_locator_strategy: pstr_locator_strategy is the type of locator('XPATH', 'ID', 'NAME','CSS_SELECTOR', 'TAG_NAME', 'LINK_TEXT' and 'PARTIAL_LINK_TEXT')
        :type pstr_locator_strategy: String

        """
        if pstr_locator_strategy.upper() not in self.locator_strategies:
            raise Exception("Unsupported locator strategy - " + pstr_locator_strategy.upper() + "! " +
                            "Supported locator strategies are 'XPATH', 'ID', 'NAME', "
                            "'CSS_SELECTOR', 'TAG_NAME', 'LINK_TEXT' , 'CLASS_NAME' and 'PARTIAL_LINK_TEXT'")
        else:
            return getattr(By, pstr_locator_strategy.upper())




    def verify_url(self,pstr_old_url, pstr_current_url):
        try:
            if 'https' in pstr_current_url:
                pstr_current_url = pstr_current_url.replace('https://','')
            elif 'http' in pstr_current_url:
                pstr_current_url = pstr_current_url.replace('http://','')

            regex = "^[{]?[0-9a-fA-F]{8}" + "-([0-9a-fA-F]{4}-)" + "{3}[0-9a-fA-F]{12}[}]?$"
            p = re.compile(regex)
            if (re.search(p, pstr_current_url.split('/')[-1])):
                pstr_current_url = pstr_current_url.replace('/' + pstr_current_url.split('/')[-1], '')
            if pstr_current_url in pstr_old_url:
                self.logger.info("URL is correct")
                return True
            else:
                self.logger.info("URL is incorrect")
                return False
        except Exception as e:
            self.logger.info(e)
            raise

    def select_dropdown_value(self, plocator, **kwargs):
        """
        Description:
            |  this method is to used to select values from drop downs . Please note this method will work for elements with "select" tag
        :param plocator: plocator is the locator of the dropdown
        :type plocator: String
        """
        select_web_element = Select(self.get_clickable_web_element(plocator))

        if "visible_text" in kwargs:
            select_web_element.select_by_visible_text(kwargs.get("visible_text"))
        elif "value" in kwargs:
            select_web_element.select_by_value(kwargs.get("value"))
        elif "index" in kwargs:
            select_web_element.select_by_index(kwargs.get("index"))
        else:
            raise Exception("No valid parameter passed")

    def wait_for_invisibility_web_element(self, locator, explicit_wait=None):
        """
           Description:
           |  This method will wait until the locator passed is invisible and return True or False based on wether th elemnet is invisible or not
           |  If the explicit wait time needs to be changed from the default wait time in configuration file, updated time can be passed in parameters which will work only for this element
           """
        if explicit_wait is None:
            explicit_wait = self.explicit_wait

        locator_details = locator.split('=', 1)
        return WebDriverWait(self.driver, explicit_wait).until(
            EC.invisibility_of_element_located((self.get_locator_strategy(locator_details[0]), locator_details[1])))
