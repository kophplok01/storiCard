Feature: Switch windowExample

Scenario: Clicking a Button and Opening Another window
  Given the user is able to open the "chrome" browser on "<desktop>" resolution in "dev" environment
  When the user clicks the "Open Window" button
  Then the user should be able to see the expected text