from Autotest.izSelenium import Selector, By
from keep import GetDriver
driver = GetDriver()

s_label_name = Selector(By.XPATH, "//input[@aria-label = 'יש להזין את שם התווית']")
def label_name():
    return driver.find(s_label_name)

s_label_exists = Selector(By.CSS_SELECTOR, ".mQXP-L9AdLc-oKdM2c-MPu53c")
def label_exists():
    return driver.find(s_label_exists)

s_new_label = Selector(By.CSS_SELECTOR, ".RmniWd-mQXP-Bz112c")
def new_label():
    return driver.find(s_new_label)