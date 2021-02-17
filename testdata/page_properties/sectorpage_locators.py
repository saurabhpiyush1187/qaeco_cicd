"""          Description:
            	|  This class contains the specific homepage locators
    """
class Sectorjobs:
    """
            Description:
            	|  This class contains the locators for home page

    """
    pstr_selected_sector = "xpath=//button[contains(.,'{0}')]/following-sibling::div//em[contains(text(),'{1}')]"
    pstr_sector_head = "xpath=//h1[contains(.,'{0}')]"
    pstr_list_job ="xpath=//h3[@class='lister__header']/a"






