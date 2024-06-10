import time

import pytest

from pages.localhost import Localhost
from pages.signup import SignUp
from pages.localhost_login import Login


# проверка регистрации
@pytest.mark.skip
def test_sign_up(browser):
    localhost_page = Localhost(browser)
    signup_page = SignUp(browser)
    login_page = Login(browser)


    localhost_page.visit()
    time.sleep(2)
    localhost_page.sign_up.click_force()
    time.sleep(2)
    assert signup_page.equal_url()
    signup_page.email.send_keys('test@test.ru')
    signup_page.name.send_keys('Test')
    signup_page.password.send_keys('123456')
    signup_page.sign_up_btn.click()
    time.sleep(2)
    assert login_page.equal_url()


# проверка обязательных полей:
# 1. поле Name необязательно:
@pytest.mark.skip
def test_name(browser):
    localhost_page = Localhost(browser)
    signup_page = SignUp(browser)
    login_page = Login(browser)

    localhost_page.visit()
    time.sleep(2)
    localhost_page.sign_up.click_force()
    time.sleep(2)
    assert signup_page.equal_url()
    signup_page.email.send_keys('test2@mail.ru')
    signup_page.password.send_keys('123456')
    signup_page.sign_up_btn.click()
    time.sleep(2)
    assert login_page.equal_url()


# поля Email Password обязательны:
@pytest.mark.skip
def test_email(browser):
    localhost_page = Localhost(browser)
    signup_page = SignUp(browser)
    login_page = Login(browser)
    localhost_page.visit()
    time.sleep(2)
    localhost_page.sign_up.click_force()
    time.sleep(2)
    assert signup_page.equal_url()
    signup_page.email.send_keys('test3@mail.ru')
    signup_page.name.send_keys('Test')
    signup_page.sign_up_btn.click()
    time.sleep(2)
    assert not login_page.equal_url()

def test_email(browser):
    localhost_page = Localhost(browser)
    signup_page = SignUp(browser)
    login_page = Login(browser)

    localhost_page.visit()
    time.sleep(2)
    localhost_page.sign_up.click_force()
    time.sleep(2)
    assert signup_page.equal_url()
    signup_page.name.send_keys('Test')
    signup_page.password.send_keys('123456')
    signup_page.sign_up_btn.click()
    time.sleep(2)
    assert not login_page.equal_url()




