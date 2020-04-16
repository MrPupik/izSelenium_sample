from behave import given, when, then
from keep.FW.navigation import login
from keep.FW.note import write_text_note, validate_new_note


@given('keep application is open on any screen')
def open_keep(context):
    print("opening app")
    assert login(), 'login failed'


@when('i enter some text at "new note" component and hit "close"')
def create_text_note(context):
    print("enter text and hit close button") 
    assert write_text_note("hello"), 'error creating text note'


@then('a new note is created that contains my text')
def validate_note(context):
    print("check note exitst and contain text")
    assert validate_new_note("hello"), 'new note could not be validated'