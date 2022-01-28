Feature: Internal Mail

  Scenario: Send an internal mail (a1)
    Given a user logged on Lead’s platform, on internal mail page #1
    When the user fill the required fields on tab ‘New message’ and send the mail
    Then the system adds the submission to the sent list

  Scenario: Clear the sent list (a2)
    Given a user logged on Lead’s platform, on internal mail page #2
    When the user selects all items from the sent list, clicks on “Delete” and confirm the exclusion
    Then the system shows the empty sent list
