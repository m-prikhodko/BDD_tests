Feature: Logo on the main page

  Scenario: Logo presence on the main page
    Given launch chrome browser
    When open web site main page
    Then logo is on the main page
    And close browser
