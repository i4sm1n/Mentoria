Feature: Language

  Scenario: Change the language to English (a3)
    Given a user logged on Lead’s platform, on edit profile page #1
    When modify the field ‘Escolha o idioma’ to ‘Inglês’ and save the change
    Then the system notifies the change and updates the page to English language

  Scenario: Change the language to Portuguese (a4)
    Given a user logged on Lead’s platform, on edit profile page #2
    When modify the field ‘Choose your language’ to ‘Portuguese’ and save the change
    Then the system notifies the change and updates the page to Portuguese language