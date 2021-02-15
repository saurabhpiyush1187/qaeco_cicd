import pytest
from pageObjects.ui.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from core.ui.ui_helper import UIHelper
from pageObjects.ui.CreateCardPage import CreateCard
from pageObjects.ui.BoardPage import BoardPage


class Test_UI_springboard:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger=LogGen.loggen()
    create_boardURL = ReadConfig.getvaluesfrom_json('page_urls', 'create_board')
    create_board_title = ReadConfig.getvaluesfrom_json('title', 'create_board')
    str_page_header = ReadConfig.getvaluesfrom_json('header', 'create_board')
    session_name = ReadConfig.getvaluesfrom_json('create-board_data', 'session_name')
    owner= ReadConfig.getvaluesfrom_json('create-board_data', 'owner')
    success_message = ReadConfig.getvaluesfrom_json('create-board_data', 'success_message')
    board_url= ReadConfig.getvaluesfrom_json('page_urls', 'board_page')
    card_type_went_well = ReadConfig.getvaluesfrom_json('card_type', 'green')
    card_type_not_went_well = ReadConfig.getvaluesfrom_json('card_type', 'red')
    card_modal_header = ReadConfig.getvaluesfrom_json('header', 'sprint_board_modal')
    well_add_card_title = ReadConfig.getvaluesfrom_json('went_well_data', 'title')
    well_add_card_description = ReadConfig.getvaluesfrom_json('went_well_data', 'description')
    well_card_activity = ReadConfig.getvaluesfrom_json('card_activity','went_well')
    well_like_count = ReadConfig.getvaluesfrom_json('card_activity','like_count')
    not_well_add_card_title = ReadConfig.getvaluesfrom_json('not_went_well_data', 'title')
    not_well_add_card_description = ReadConfig.getvaluesfrom_json('not_went_well_data', 'description')
    not_well_expected_desc = ReadConfig.getvaluesfrom_json('not_went_well_data','description_displayed')
    not_well_card_activity = ReadConfig.getvaluesfrom_json('card_activity','not went well')
    not_well_delete_header = ReadConfig.getvaluesfrom_json('not_went_well_data','delete_header')
    not_well_delete_question = ReadConfig.getvaluesfrom_json('not_went_well_data','delete_question')

    @pytest.mark.smoke
    @pytest.mark.ui
    def test_login_create_board(self, setup):
        self.logger.info("****Started create board Test****")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.bp = BoardPage(self.driver)
        # login to application and verify homepage
        assert self.lp.login(self.username, self.password)
        # go to create board link
        self.bp.go_to_create_board()
        self.ui_helper = UIHelper(self.driver)
        pstr_url = self.driver.current_url
        # verify current url of create board
        assert self.ui_helper.verify_url(self.create_boardURL, pstr_url)
        pstr_title = self.driver.title
        # verify title of create board page
        assert self.create_board_title, pstr_title
        # verify header of create board page
        assert self.bp.verify_page_header(self.str_page_header)
        # verify board creation with success message created
        bln_final_result = self.bp.create_board(self.session_name, self.owner, self.success_message)
        if bln_final_result:
            self.logger.info("*** Test 001 passed****")
            self.logger.info("****Create board Test End****")
            self.driver.quit()
            assert True
        else:
            self.logger.error("****Test 001 failed****")
            self.logger.info("****Create board Test End****")
            self.driver.quit()
            assert False



    @pytest.mark.smoke
    @pytest.mark.ui
    def test_card_manipulation(self,setup):
        self.logger.info("****Started Card manipulation Test****")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.bp = BoardPage(self.driver)
        #login to application and verify homepage
        assert self.lp.login(self.username,self.password)
        #go to create board link
        self.bp.go_to_create_board()
        #create board and verify it
        bln_final_result = self.bp.create_board(self.session_name,self.owner,self.success_message)
        if bln_final_result:
            self.ui_helper = UIHelper(self.driver)
            self.cp = CreateCard(self.driver)
            self.cp.wait_board_page_to_load()
            pstr_url = self.driver.current_url
            #verify board url
            assert self.ui_helper.verify_url(self.board_url, pstr_url)
            #click went well card card
            self.cp.clickCard(self.card_type_went_well)
            #verify modal header
            assert self.cp.verify_modal_header(self.card_modal_header)
            #create went well card
            self.cp.create_card(self.well_add_card_title,self.well_add_card_description)
            #verify well card creation
            assert self.cp.verify_card(self.card_type_went_well, self.well_add_card_title,self.well_add_card_description)
            #click did'nt go well card
            self.cp.clickCard(self.card_type_not_went_well)
            #verify modal header
            assert self.cp.verify_modal_header(self.card_modal_header)
            #create didn't go well card
            self.cp.create_card(self.not_well_add_card_title, self.not_well_add_card_description)
            #verify didn't go well card
            assert self.cp.verify_card(self.card_type_not_went_well,self.not_well_add_card_title, self.not_well_expected_desc)
            #like the went well card
            self.cp.click_activity(self.card_type_went_well,self.well_card_activity)
            #verify like
            bln_like= self.cp.verify_activity(self.card_type_went_well,self.well_card_activity,pstr_like_count =self.well_like_count)
            #delete the didn't go well card
            self.cp.click_activity(self.card_type_not_went_well,self.not_well_card_activity)
            #verify card delete modal
            assert self.cp.verify_delete_modal(self.not_well_delete_header, self.not_well_delete_question)
            #confirm card delete
            self.cp.delete_card()
            #verify didn't go well card is deleted
            bln_delete_card = self.cp.verify_delete_card(self.card_type_not_went_well)
            if bln_like and bln_delete_card:
                self.logger.info("***Test 002 passed****")
                self.logger.info("*** Card manipulation test ended****")
                self.driver.quit()
                assert True
            else:
                self.logger.error("****Test 002 failed ****")
                self.logger.info("*** Card manipulation test ended****")
                self.driver.quit()
                assert False
        else:
            self.logger.error("****Test 002 failed Board not created****")
            self.logger.info("*** Card manipulation test ended****")
            self.driver.quit()
            assert False








