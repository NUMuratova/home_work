from pages.base_page import BasePage
from components.components import WebElement


class Login(BasePage):

    def __init__(self, driver):
        self.base_url = 'http://localhost:5000/login'
        super().__init__(driver, self.base_url)

        self.your_email = WebElement(driver, 'body > section > div.hero-body > div > div > div > form > div:nth-child(1) > div > input')
        self.your_password = WebElement(driver, 'body > section > div.hero-body > div > div > div > form > div:nth-child(2) > div > input')
        self.remember_me = WebElement(driver, 'body > section > div.hero-body > div > div > div > form > div:nth-child(3) > label > input[type=checkbox]')
        self.login_btn = WebElement(driver, 'body > section > div.hero-body > div > div > div > form > button')
        self.notification = WebElement(driver, 'body > section > div.hero-body > div > div > div > div')


