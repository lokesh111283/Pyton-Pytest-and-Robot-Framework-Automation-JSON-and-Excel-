import pytest
from selenium import webdriver
from PythonSeleniumFramework.BaseClass import Baseclass
from PythonSeleniumFramework.LoginDetails import LoginDetails
from PythonSeleniumFramework.LogoutDetails import LogoutDetails

#The below class gets the data from JSON and verifies if login an logout are working as expected and verification
#is done post login and post logout
class TestLoginMain(Baseclass):
    def test_main(self,getdata):
        log = self.getLogger()
        print("browser gets invoked")
        login_details=LoginDetails(self.driver)
        login_details.getloc_id().send_keys(getdata["username"])
        login_details.getloc_pwd().send_keys(getdata["password"])
        login_details.getloc_signin_Button().click()
        self.verify_if_login_locator_available(login_details.var_in_conf)
        login_text =login_details.getloc_in_conf().text
        log.info("login successful")
        print(login_text)
        assert login_text == "AUTOMATION"
        logout_details=LogoutDetails(self.driver)
        logout_details.getloc_sign_out().click()
        log.info("logout successful")
        self.verify_if_logout_locator_available(logout_details.var_sign_out_conf)
        logout_text = logout_details.getloc_sign_out_conf().text
        assert logout_text == "Log in"
        self.driver.refresh









