"""          Description:
            	|  This class contains the specific homepage locators
    """
class Joblocators:
    """
            Description:
            	|  This class contains the locators for home page

    """
    pstr_verify_home_page = "xpath=//img[@title='{0}']"
    pstr_nav_list ="//ul[@class='primary-nav__items togglable-nav__items cf']/li"
    pstr_search_list="//input[@type='text']"
    pstr_sector_list="//div[@class='browse__items']/ul/li/a"
    pstr_nav_links="xpath=//a[contains(text(),'{0}')]"
    pstr_nav_head ="xpath=//h1[contains(.,'{0}')]"





