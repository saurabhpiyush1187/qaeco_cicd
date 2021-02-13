"""          Description:
            	|  This class contains the specific card page locators
    """
class cardlocators:
    """
            Description:
            	|  This class contains the locators for create card page

    """
    pstr_type_card= 'xpath=//button[contains(text(),"{0}")]/parent::div/parent::h5/following-sibling::div/button[@type="button"]'
    pstr_didnt_go_well = 'xpath=//button[contains(.,"go well")]/parent::div/parent::h5/following-sibling::div/button[@type="button"]'
    pstr_addcard_model = 'xpath=//div[@id="add-card-modal" and contains(text(),"{0}")]'
    pstr_title = 'xpath=//input[@placeholder="Required"]'
    pstr_description = 'xpath=//textarea[@placeholder="Optional"]'
    pstr_addcard_button ='xpath=//button[contains(text(),"Add Card")]'
    pstr_load_title='xpath=//button[contains(text(),"{0}")]/parent::div/parent::h5/following-sibling::div/button[@type="button"]/parent::div//h6'
    pstr_verify_title ='//button[contains(text(),"{0}")]/parent::div/parent::h5/following-sibling::div/button[@type="button"]/parent::div//h6'
    pstr_verify_description ='//button[contains(text(),"{0}")]/parent::div/parent::h5/following-sibling::div/button[@type="button"]/parent::div//div/p'
    pstr_activity ='xpath=//button[contains(text(),"{0}")]/parent::div/parent::h5/following-sibling::div/button[@type="button"]/parent::div//li/button[contains(text(),"{1}")]'
    pstr_verify_activity = '//button[contains(text(),"{0}")]/parent::div/parent::h5/following-sibling::div/button[@type="button"]/parent::div//li[{1}]/button'
    pstr_delete_pop_up = 'xpath=//div[contains(text(),"Delete Card")]'
    pstr_verify_delete_pop_up = '//div[@class="modal-title h4"]'
    pstr_verify_delete_question = '//div[@class="modal-body"]/p'
    pstr_confirm_delete ='xpath=//button[contains(text(),"Confirm")]'