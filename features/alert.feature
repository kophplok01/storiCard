@alert

Feature: Feature: Handling alerts


  @alert-dialog
  Scenario: Handling alert dialog
    Given the user is able to open the "chrome" browser on "mobile" resolution in "dev" environment
    When the user types "Stori Card" and clicks the "alert" button
    Then the user prints the text in the alert and clicks on OK

  @confirm-dialog
  Scenario: Handling confirm dialog
    Given the user is able to open the "chrome" browser on "mobile" resolution in "dev" environment
    When the user types "Stori Card" and clicks the "confirm" button
    Then the user prints the text in the confirm alert
    And the user confirms that the alert text is equal to "Hello Stori Card, Are you sure you want to confirm?" and then click ok
