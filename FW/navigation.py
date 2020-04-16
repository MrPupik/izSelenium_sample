from time import sleep

from Autotest.izSelenium import GetDriver
import Autotest.Core.TimeoutManager as TM
import keep.FW.Selectors.SC_login as SC_login
import keep.FW.Selectors.SC_generics as SC_generics
from keep import GetDriver
driver = GetDriver()


def login():
    driver.get("https://keep.google.com/u/0/")
    driver.maximize_window
    SC_login.user_name().send_keys("autotest141")
    SC_login.user_next_button().click()
    sleep(0.2)
    TM.Long_timeout(4)
    SC_login.user_password().click()
    SC_login.user_password().send_keys("Pinpazil1")
    sleep(0.2)
    SC_login.user_psw_button().click()
    return SC_generics.main_icon(True) is not None
