
import Autotest.Core.TimeoutManager as TM
from keep.FW.navigation import login
from keep.FW.Selectors.SC_notes import new_note, close_button, reminder
from keep.FW.Selectors.SC_notes import note_options, add_label
from keep.FW.Selectors.SC_reminder import tommorow
from keep.FW.Selectors.SC_labels import label_name

from keep.FW.note import edit_text_note

login()


def write_note():
    # creating a new note
    n = new_note()
    n.click()
    n.send_keys("hello")

    # setting a reminder
    note_options("תזכורת").click()
    TM.Short_timeout()
    tommorow().click()

    # adding a label
    note_options("עוד").click()
    TM.Short_timeout()
    add_label().click()
    TM.Short_timeout()
    label_name().send_keys("label")
    from selenium.webdriver.common.keys import Keys
    label_name().send_keys(Keys.ENTER)

    # closing the new note option
    b = close_button()
    b.click()


write_note()
edit_text_note("hello")
