Feature: delete keep notes

  Scenario: delete a note
    Given I have a note I want to delele
    When I select the "delete note" option
    Then the note is deleted

