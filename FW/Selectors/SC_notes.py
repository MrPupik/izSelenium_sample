from Autotest.izSelenium import Selector, By
from keep import GetDriver
driver = GetDriver()

s_new_note = Selector(By.XPATH, "//div[@aria-label='רישום הערה…']")
def new_note():
    return driver.find(s_new_note)

s_new_list = Selector(By.XPATH, "//div[@aria-label='רשימה חדשה']")
def new_list():
    return driver.find(s_new_list)

s_close_button = Selector(By.XPATH, "//div[contains(text(),'סגירה')]")
def close_button():
    return driver.find(s_close_button) 

def note_options(option_name):
    s_option = Selector(By.XPATH, "//div[@class = 'h1U9Be-xhiy4']//div[@aria-label='" + option_name +"']")
    return driver.find(s_option)

s_add_label = Selector(By.XPATH, "//div[@id = ':2']")
def add_label():
    return driver.find(s_add_label)

s_delete_note = Selector(By.XPATH, "//div[@id = ':1']")
def delete_note():
    return driver.find(s_delete_note)


s_notes_list = Selector(By.CSS_SELECTOR, ".IZ65Hb-n0tgWb.IZ65Hb-WsjYwc-nUpftc.di8rgd-r4nke.RNfche")
def notes_list():
    return driver.finds(s_notes_list)

def specific_note(note_text):
    s_note = Selector(By.XPATH, "//div[@class='IZ65Hb-n0tgWb IZ65Hb-WsjYwc-nUpftc di8rgd-r4nke RNfche']//div[@role='textbox' and contains(text(), '" + note_text +"')]")
    return driver.find(s_note)

def edit_note_options(option_name):
    # Needs to click a specific note first
    s_edit_option = Selector(By.XPATH, "//div[@class = 'IZ65Hb-n0tgWb di8rgd-r4nke IZ65Hb-QQhtn oT9UPb']//div[@aria-label='" + option_name +"']")
    return driver.find(s_edit_option)

s_note_textbox = Selector(By.XPATH, "//div[@class = 'VIpgJd-TUo6Hb XKSfm-L9AdLc eo9XGd']//div[@role='textbox']")
def note_textbox():
    return driver.find(s_note_textbox)

s_edit_close_button = Selector(By.XPATH, "//div[@class = 'VIpgJd-TUo6Hb XKSfm-L9AdLc eo9XGd']//div[contains(text(),'סגירה')]")
def edit_close_button():
    return driver.find(s_edit_close_button)
