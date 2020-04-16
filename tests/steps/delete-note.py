from behave import given, when, then

@given('I have a note I want to delele')
def check_for_note(context):
    print("there is a note")

@when('I select the "delete note" option')
def deleting_note(context):
    print("deleting note")

@then('the note is deleted')
def check_if_deleted(context):
    print("the note was deleted")
    