from Autotest.izSelenium import Selector, By
from keep import GetDriver
driver = GetDriver()

s_main_icon = Selector(By.CSS_SELECTOR, "#ognwrapper a[aria-label='Keep']")
def main_icon(sensitive=False):
    return driver.find(s_main_icon, sensitive)