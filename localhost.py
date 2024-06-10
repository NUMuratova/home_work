from pages.base_page import BasePage
from components.components import WebElement


class Localhost(BasePage):

    def __init__(self, driver):
        self.base_url = 'http://localhost:5000'
        super().__init__(driver, self.base_url)

        self.sign_up = WebElement(driver, '#navbarMenuHeroA > div > a:nth-child(3)')
        self.login = WebElement(driver, '#navbarMenuHeroA > div > a:nth-child(2)')

