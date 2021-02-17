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
    login_url= ReadConfig.getvaluesfrom_json('page_urls', 'login_url')
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



    @pytest.fixture()
    def launch_app(self,setup):
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.driver.maximize_window()
        self.driver.get(self.baseURL + self.login_url)
        # login to application and verify homepage
        assert self.lp.login(self.username, self.password)

    @pytest.mark.smoke
    @pytest.mark.ui
    def test_springboard(self, launch_app):
        self.bp = BoardPage(self.driver)
        self.cp = CreateCard(self.driver)
        self.ui_helper = UIHelper(self.driver)
        self.login_create_board()
        self.card_manipulation()


    def login_create_board(self):
        self.logger.info("****Started create board Test****")
        # go to create board link
        self.bp.go_to_create_board()
        pstr_url = self.driver.current_url
        # verify current url of create board
        assert self.ui_helper.verify_url(self.baseURL+self.create_boardURL, pstr_url)
        pstr_title = self.driver.title
        # verify title of create board page
        assert self.create_board_title, pstr_title
        # verify header of create board page
        assert self.bp.verify_page_header(self.str_page_header)
        # verify board creation with success message created
        bln_final_result = self.bp.create_board(self.session_name, self.owner, self.success_message)
        if bln_final_result:
            self.logger.info("*** Board created successfully****")
            self.logger.info("****Create board Test End****")
            assert True
        else:
            self.logger.error("****Board creation unsuccessful****")
            self.logger.info("****Create board Test End****")
            assert False


    def card_manipulation(self):
        self.logger.info("****Started Card manipulation Test****")
        self.cp.wait_board_page_to_load()
        pstr_url = self.driver.current_url
        #verify board url
        assert self.ui_helper.verify_url(self.baseURL+self.board_url, pstr_url)
        #click went well card card
        self.cp.clickCard(self.card_type_went_well)
        #verify modal header
        assert self.cp.verify_modal_header(self.card_modal_header)
        #create went well card
        self.cp.create_card(self.well_add_card_title,self.well_add_card_description)
        #verify well card creation
        assert self.cp.verify_card(self.card_type_went_well, self.well_add_card_title,self.well_add_card_description)
        self.cp.wait_board_page_to_load()
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
            self.logger.info("***Card manipulation Successful****")
            self.logger.info("*** Card manipulation test ended****")
            assert True
        else:
            self.logger.error("****Card manipulation unsuccessful****")
            self.logger.info("*** Card manipulation test ended****")
            assert False