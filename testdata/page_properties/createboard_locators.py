"""          Description:
            	|  This class contains the specific homepage locators
    """
class Boardlocators:
    """
            Description:
            	|  This class contains the locators for home page

    """
    pstr_input_session_name = "xpath=//input[@placeholder='Session Name']"
    pstr_owner_drop_down = "xpath=//select[contains(.,'Choose Owner')]"
    pstr_createboard_button = "xpath=//button[contains(.,'Create Board')]"
    pstr_page_header ="xpath=//div/h1[contains(text(),'{0}')]"
    pstr_pop_up ="xpath=//div[@class='swal-title']"