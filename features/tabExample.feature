@newTab

Feature: Switch tabExample

  @new-tab-expected
  Scenario: Clicking a new tab Button and see the expected view
    Given the user is able to open the "chrome" browser on "mobile" resolution in "dev" environment
    When the user clicks the "Open tab" button
    Then the user should be able to see the expected button