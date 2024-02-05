
import logging
import time

import utilities.custom_logger as cl
from base.basepage import BasePage


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _username_field = "//input[@name='username']"
    _password_field = "//input[@name='password']"
    _login_button = "//button[contains(text(), Login)]"
    _nav_drop = "//span[@class='oxd-userdropdown-tab']"
    _logout_button = "//a[@href='/web/index.php/auth/logout']"

    def enterUsername(self, username):
        self.sendKeys(username, self._username_field, locatorType="xpath")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType="xpath")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, username="", password=""):
        self.enterUsername(username)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//img[@alt='profile picture']", locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[@role='alert']//p[.='Invalid credentials']", locatorType="xpath")
        return result

    def logout(self):
        self.elementClick(self._nav_drop, locatorType="xpath")
        time.sleep(1)
        self.elementClick(self._logout_button, locatorType="xpath")


