from testdata.page_properties.create_card_locators import cardlocators
from utilities.customLogger import LogGen
import os
from utilities.readProperties import ReadConfig
from core.ui.ui_helper import UIHelper
import time

class CreateCard:
    # Create card Page
    card_locators = cardlocators()
    logger = LogGen.loggen()
    explicit_wait = ReadConfig.getexplicitwait()

    def __init__(self,driver):
        self.driver=driver
        self.ui_helper = UIHelper(self.driver)


    def clickCard(self, pstr_type):
        pstr_card_type = self.card_locators.pstr_type_card.format(pstr_type)
        time.sleep(3)
        bln_card_type = self.ui_helper.is_element_displayed(pstr_card_type)
        if bln_card_type:
            self.ui_helper.click(pstr_card_type)
            self.logger.info("****Card type is clicked****  " + pstr_type)
            assert True
        else:
            self.logger.info("****card type not found or not clickable****")
            self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_login_createCard.png")
            self.driver.quit()
            assert False



    def verify_modal_header(self, pstr_header):
        pstr_card_type = self.card_locators.pstr_addcard_model.format(pstr_header)
        bln_card_type = self.ui_helper.is_element_displayed(pstr_card_type)
        if bln_card_type:
            self.logger.info("****Card Modal header verified****  " + pstr_header)
            return True
        else:
            self.logger.info("****Card Modal header not verified****Please see screenshot")
            self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_login_modal_header.png")
            self.driver.quit()
            return False


    def wait_board_page_to_load(self):
        bln_card_page= self.ui_helper.is_element_displayed(self.card_locators.pstr_didnt_go_well)
        if bln_card_page:
            self.logger.info("****Card creation page loaded****")
            assert True
        else:
            self.logger.info("****Delay in page loading****Please see screenshot")
            self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_login_create_board_fail.png")
            self.driver.quit()
            assert False

    def create_card(self,pstr_title, pstr_description):
        self.driver.implicitly_wait(3)
        bln_title_name = self.ui_helper.is_element_displayed(self.card_locators.pstr_title)
        if bln_title_name:
            self.ui_helper.type(self.card_locators.pstr_title,pstr_title)
            self.logger.info("****Entered title name****   " + str(pstr_title))
        else:
            self.logger.info("****Unable to enter title name****")
            self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_login_createCard_title.png")
            self.driver.quit()
            return False

        bln_description = self.ui_helper.is_element_displayed(self.card_locators.pstr_description)
        if bln_description:
            self.ui_helper.type(self.card_locators.pstr_description, pstr_description)
            self.logger.info("****Entered Description****   " + str(pstr_description))
        else:
            self.logger.info("****Unable to enter description****")
            self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_login_createCard_title.png")
            self.driver.quit()
            return False

        bln_submit_create_card = self.ui_helper.is_element_displayed(self.card_locators.pstr_addcard_button)
        if bln_submit_create_card:
            self.ui_helper.click(self.card_locators.pstr_addcard_button)
            self.logger.info("****Clicked Add a card button***")
        else:
            self.logger.info("****Unable to click Add a card button****")
            self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_login_createBoard_button.png")
            self.driver.quit()
            return False


    def verify_card(self,pstr_card_type,pstr_title,pstr_desciption):
        pstr_load = self.card_locators.pstr_load_title.format(pstr_card_type)
        bln_load_card = self.ui_helper.is_element_displayed(pstr_load)
        if bln_load_card:
            pstr_expected_title= self.card_locators.pstr_verify_title.format(pstr_card_type)
            str_pstr_title = self.driver.find_element_by_xpath(pstr_expected_title).text
            pstr_expected_descr = self.card_locators.pstr_verify_description.format(pstr_card_type)
            str_pstr_desc = self.driver.find_element_by_xpath(pstr_expected_descr).text

            if str_pstr_title==pstr_title and str_pstr_desc==pstr_desciption:
                self.logger.info("****Card Details verified****")
                return True
            else:
                self.logger.info("****Unable to verify card details****")
                self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_login_createcard_details_verify_fail.png")
                self.driver.quit()
                return False
        else:
            self.logger.info("****Error in creating card****")
            self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_login_createcard_details_verify_fail.png")
            self.driver.quit()
            return False

    def click_activity(self,pstr_card_type, pstr_activity):
        time.sleep(3)
        if pstr_activity == "like":
            pstr_activity_val = "0"
        else:
            pstr_activity_val = pstr_activity
        pstr_activity_actual = self.card_locators.pstr_activity.format(pstr_card_type,pstr_activity_val)
        bln_pstr_activity = self.ui_helper.is_element_displayed(pstr_activity_actual)
        if bln_pstr_activity:
            self.ui_helper.click(pstr_activity_actual)
            self.logger.info(pstr_activity +"****Activity clicked****")
            assert True
        else:
            self.logger.info("****Error in clicking activity****")
            self.driver.save_screenshot(
                "." + os.sep + "Screenshots" + os.sep + "test_login_createcard_click_activity_verify_fail.png")
            self.driver.quit()
            assert False


    def verify_activity(self,pstr_card,pstr_activity,**kwargs):
        if pstr_activity == "like" and "pstr_like_count" in kwargs:
            pstr_activity_val = kwargs.get("pstr_like_count")
            pstr_activity_actual = self.card_locators.pstr_activity.format(pstr_card, pstr_activity_val)
            bln_pstr_activity = self.ui_helper.is_element_displayed(pstr_activity_actual)
            if bln_pstr_activity:
                self.logger.info(pstr_activity + "**** is verified****")
                return True
            else:
                pstr_list =3
                pstr_actual_like = self.card_locators.pstr_verify_activity.format(pstr_card,pstr_list)
                str_actual_like = self.driver.find_element_by_xpath(pstr_actual_like).text
                self.logger.info("****Like not verified****" + "Actual Like is " + str_actual_like)
                self.driver.save_screenshot(
                    "." + os.sep + "Screenshots" + os.sep + "test_login_createcard_like_activity_verify_fail.png")
                self.driver.quit()
                return False

    def verify_delete_modal(self, pstr_delete_header, pstr_delete_question):
        bln_delete_pop_up = self.ui_helper.is_element_displayed(self.card_locators.pstr_delete_pop_up)
        if bln_delete_pop_up:
            str_delete_header = self.driver.find_element_by_xpath(self.card_locators.pstr_verify_delete_pop_up).text
            str_delete_question = self.driver.find_element_by_xpath(self.card_locators.pstr_verify_delete_question).text

            if str_delete_header==pstr_delete_header and str_delete_question==pstr_delete_question:
                self.logger.info("****Delete modal pop up is verified****")
                return True
            else:
                self.logger.info("****Delete modal pop up is not verified****")
                self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_verify_delete.png")
                self.driver.quit()
                return False
        else:
            self.logger.info("****Delete modal pop up not showning up****")
            self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_verify_delete.png")
            self.driver.quit()
            return False


    def delete_card(self):
        bln_confirm_delete =self.ui_helper.is_element_displayed(self.card_locators.pstr_confirm_delete)
        if bln_confirm_delete:
            self.ui_helper.click(self.card_locators.pstr_confirm_delete)
            self.logger.info("****Card delete button is clicked****")
            assert True
        else:
            self.logger.info("****Delete modal pop up not showning up****")
            self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_verify_delete.png")
            self.driver.quit()
            assert False

    def verify_delete_card(self,pstr_card_type):
        pstr_load = self.card_locators.pstr_load_title.format(pstr_card_type)
        bln_load_card = self.ui_helper.wait_for_invisibility_web_element(pstr_load)
        if bln_load_card:
            self.logger.info("****Card is deleted****")
            return True
        else:
            self.logger.info("****Card is still showing up****")
            self.driver.save_screenshot("." + os.sep + "Screenshots" + os.sep + "test_verify_delete_card.png")
            self.driver.quit()
            return False



