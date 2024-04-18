Feature: iframe

  Scenario: Search for specific text  in an iframe
    Given the user is able to open the "chrome" browser on "mobile" resolution in "dev" environment
    When I switch to the iframe
    Then the user search for an specific text
