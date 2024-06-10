import time

import pytest

from pages.localhost import Localhost
from pages.localhost_login import Login
from pages.localhost_profile import Profile


#проверка авторизации (заполняем все поля):
@pytest.mark.skip
def test_login(browser):
    localhost_page = Localhost(browser)
    login_page = Login(browser)
    profile_page = Profile(browser)

    localhost_page.visit()
    time.sleep(2)
    localhost_page.login.click_force()
    time.sleep(2)
    #assert login_page.equal_url()

    login_page.your_email.send_keys('test@test.ru')
    login_page.your_password.send_keys('123456')
    login_page.remember_me.click()
    login_page.login_btn.click()
    time.sleep(2)
    assert profile_page.equal_url()
    assert profile_page.welcome_test.get_text() == 'Welcome, Test!'
    profile_page.logout.click()
    time.sleep(2)


#проверка обязательности поля Email:
def test_login_email(browser):
    localhost_page = Localhost(browser)
    login_page = Login(browser)
    profile_page = Profile(browser)

    localhost_page.visit()
    time.sleep(2)
    localhost_page.login.click_force()
    time.sleep(2)
    #assert login_page.equal_url()

    login_page.your_password.send_keys('123456')
    login_page.remember_me.click()
    login_page.login_btn.click()
    time.sleep(2)
    assert login_page.notification.exist()
    assert not profile_page.equal_url()
    profile_page.logout.click()
    time.sleep(2)


#проверка обязательности поля Password
@pytest.mark.skip
def test_login_password(browser):
    localhost_page = Localhost(browser)
    login_page = Login(browser)
    profile_page = Profile(browser)

    localhost_page.visit()
    time.sleep(2)
    localhost_page.login.click_force()
    time.sleep(2)
    #assert login_page.equal_url()

    login_page.your_email.send_keys('test@test.ru')
    login_page.remember_me.click()
    login_page.login_btn.click()
    time.sleep(2)
    assert login_page.notification.exist()
    assert not profile_page.equal_url()
    profile_page.logout.click()
    time.sleep(2)


#проверка обязательности чекбокса
@pytest.mark.skip
def test_login_remember_me(browser):
    localhost_page = Localhost(browser)
    login_page = Login(browser)
    profile_page = Profile(browser)

    localhost_page.visit()
    time.sleep(2)
    localhost_page.login.click_force()
    time.sleep(2)
    #assert login_page.equal_url()

    login_page.your_email.send_keys('test@test.ru')
    login_page.your_password.send_keys('123456')
    login_page.login_btn.click()
    time.sleep(2)
    assert profile_page.equal_url()
    assert profile_page.welcome_test.get_text() == 'Welcome, Test!'
    profile_page.logout.click()





