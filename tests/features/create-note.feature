Feature: create keep notes

  @sanity @text
  Scenario: create a text note
    Given keep application is open on any screen
     When i enter some text at "new note" component and hit "close"
     Then a new note is created that contains my text


