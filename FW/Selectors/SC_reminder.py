from Autotest.izSelenium import Selector, By
from keep import GetDriver
driver = GetDriver()

s_later_today = Selector(By.XPATH, "//div[@id = ':4e']")
def later_today():
    return driver.find(s_later_today)

s_tommorow = Selector(By.XPATH, "//div[@id = ':4f']")
def tommorow():
    return driver.find(s_tommorow)

s_next_week = Selector(By.XPATH, "//div[@id = ':4g']")
def next_week():
    return driver.find(s_next_week)

# make it work later (choosing date or location)
s_selecting_time = Selector(By.XPATH, "//div[@id = ':4k']")
def selecting_time():
    return driver.find(s_selecting_time) 

s_selecting_location = Selector(By.XPATH, "//div[@id = ':4l']")
def selecting_location():
    return driver.find(s_selecting_location) 