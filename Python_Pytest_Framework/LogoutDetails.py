from selenium.webdriver.common.by import By

# Below are the locators information and getter methods created so that main rogram can access them
class LogoutDetails:

    def __init__(self,driver):
        self.driver=driver;

    loc_sign_out = (By.XPATH, "//button[normalize-space()='Sign Out']")
    loc_sign_out_conf = (By.CSS_SELECTOR, ".login-title")
    var_sign_out_conf = ".login-title"

    def getloc_sign_out(self):
        return self.driver.find_element(*LogoutDetails.loc_sign_out)

    def getloc_sign_out_conf(self):
        return self.driver.find_element(*LogoutDetails.loc_sign_out_conf)



