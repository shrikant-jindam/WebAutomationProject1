import datetime
import os
import time
import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test001_login:
    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = "secret_sauce"

    logger = LogGen.logGen()

    @pytest.mark.sanity
    def test_loginpageTesting(self,setup):

        self.logger.info("******************* Test001 Login ************************")
        self.logger.info("******************** Testing login page  *****************************")
        self.driver = setup
        self.driver.get(self.base_url)
        url = self.driver.current_url
        self.driver.close()
        if url == self.base_url:
            assert True
        else:
            assert False

    @pytest.mark.regression
    def test_login_username_password(self,setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual = self.driver.current_url
        self.logger.info("Checking current page url")
        if actual == "https://www.saucedemo.com/inventory.html1":
            assert True
            self.logger.info("*****************Test case Passed****************")
            self.logger.info("Screenshot saved....")
            self.driver.save_screenshot("C:/Users/Admin/PycharmProjects/WebAutomationProject1/Screenshots/SS0001.png")
            self.logger.info("Webdiver closing....")
            self.driver.close()
        else:
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_DDT_test(self,setup):
        self.driver = setup
        self.driver.get(self.base_url)
        time.sleep(5)
        current = datetime.datetime
        print(str(current)+"shrikant")
        self.driver.save_screenshot("C:/Users/Admin/PycharmProjects/ECommerce_Testing/Screenshots/"+"SS"+str(datetime.time)+".png")
        self.driver.close()

