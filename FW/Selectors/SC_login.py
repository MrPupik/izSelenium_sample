from Autotest.izSelenium import Selector, By
from keep import GetDriver
driver = GetDriver()

s_user_name = Selector(By.CSS_SELECTOR, "#identifierId")


def user_name():
    return driver.find(s_user_name)


s_user_next_button = Selector(By.XPATH, "//span[contains(text(), 'הבא')]")
def user_next_button():
    return driver.find(s_user_next_button)


s_user_password = Selector(By.XPATH, "//input[@name = 'password']")
def user_password():
    return driver.find(s_user_password)


s_psw_next_button = Selector(By.CSS_SELECTOR, ".RveJvd.snByac")
def user_psw_button():
    return driver.find(s_psw_next_button)