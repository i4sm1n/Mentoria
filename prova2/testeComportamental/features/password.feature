Feature: Change the password

  Scenario: Change the password (a5)
    Given a user logged on Lead’s platform, on edit profile page #3
    When the user fill the required fields on tab ‘Change password’ and save the change
    Then the system notifies the user that update was successful

  Scenario: Change the password (a6)
    Given a user logged on Lead’s platform, on edit profile page #4
    When the user fill the required fields on tab ‘Change password’ and save the change#
    Then the system notifies the user that update was successful#