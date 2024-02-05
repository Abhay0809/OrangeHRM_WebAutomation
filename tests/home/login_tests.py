import os
import pytest
import unittest

from ddt import ddt, data, unpack
from dotenv import load_dotenv

from pages.home.login_page import LoginPage
from utilities.read_data import getCSVData
from utilities.teststatus import TestStatus

load_dotenv()


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(*getCSVData("C:\\Users\\Abhay_Anand\\PycharmProjects\\OrangeHRM\\logindata.csv"))
    @unpack
    def test_validLogin(self, username, password):
        self.lp.login(username, password)
        result = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result, "Login was successful")

    @pytest.mark.run(order=2)
    def test_invalidLogin(self):
        self.lp.logout()
        self.lp.login(os.environ.get('w_uname'), os.environ.get('w_pwd'))
        result = self.lp.verifyLoginFailed()
        self.ts.markFinal("test_invalidLogin", result, "Login was not successful")

