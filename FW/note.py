import keep.FW.Selectors.SC_notes as SC_notes
import keep.FW.Selectors.SC_reminder as SC_reminder
import keep.FW.Selectors.SC_labels as SC_labels
import Autotest.Core.TimeoutManager as TM


def write_text_note(text):
    n = SC_notes.new_note()
    n.click()
    n.send_keys(text)
    SC_notes.close_button().click()    
    return n.waitNexist()


def validate_new_note(text):
    l = SC_notes.notes_list()
    note_title = l[0].get_text()
    return note_title == text


def delete_specific_note(note_text):
    SC_notes.specific_note(note_text).click()
    TM.Long_timeout()
    SC_notes.edit_note_options("עוד").click()
    TM.Short_timeout()
    SC_notes.delete_note().click()


def add_label_to_note(note_text):
    SC_notes.specific_note(note_text).click()
    TM.Long_timeout()
    SC_notes.edit_note_options("עוד").click()
    TM.Short_timeout()
    SC_notes.add_label().click()
    SC_labels.label_name().send_keys("label")
    from selenium.webdriver.common.keys import Keys
    SC_labels.label_name().send_keys(Keys.ENTER)
    SC_notes.edit_close_button().click()


def add_reminder_to_note(note_text):
    SC_notes.specific_note(note_text).click()
    TM.Long_timeout()
    SC_notes.edit_note_options("תזכורת").click()
    TM.Short_timeout()
    SC_reminder.later_today().click()
    SC_notes.edit_close_button().click()


def archive_note(note_text):
    SC_notes.specific_note(note_text).click()
    TM.Long_timeout()
    SC_notes.edit_note_options("שליחה לארכיון").click()


def edit_text_note(note_text):
    SC_notes.specific_note(note_text).click()
    TM.Long_timeout()
    SC_notes.note_textbox().click()
    SC_notes.note_textbox().send_keys("again")
    TM.Short_timeout()
    SC_notes.edit_close_button().click()


    
