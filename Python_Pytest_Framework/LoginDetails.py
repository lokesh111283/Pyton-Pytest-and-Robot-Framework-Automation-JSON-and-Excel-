from selenium.webdriver.common.by import By

# Below are the locators information and getter methods created so that main rogram can access them
class LoginDetails:
    def __init__(self,driver):
        self.driver=driver;

    loc_id = (By.ID,"userEmail")
    loc_pwd = (By.ID, "userPassword")
    loc_signin_Button = (By.ID,"login")
    loc_in_conf = (By.CSS_SELECTOR, "div[class='left mt-1'] h3")
    var_in_conf = "div[class='left mt-1'] h3"


    def getloc_id(self):
        return self.driver.find_element(*LoginDetails.loc_id)

    def getloc_pwd(self):
        return self.driver.find_element(*LoginDetails.loc_pwd)

    def getloc_signin_Button(self):
        return self.driver.find_element(*LoginDetails.loc_signin_Button)

    def getloc_in_conf(self):
        return self.driver.find_element(*LoginDetails.loc_in_conf)
