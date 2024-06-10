from pages.base_page import BasePage
from components.components import WebElement


class Profile(BasePage):

    def __init__(self, driver):
        self.base_url = 'http://localhost:5000/profile'
        super().__init__(driver, self.base_url)

        self.welcome_test = WebElement(driver, 'body > section > div.hero-body > div > h1')
        self.logout = WebElement(driver, '#navbarMenuHeroA > div > a:nth-child(3)')