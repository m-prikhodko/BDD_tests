Feature: Go to main page from listing

    Scenario: Going to main page from listing
    Given launch chrome browser
    When open web site listing page
    And click on logo
    Then main page is opened
    And close browser