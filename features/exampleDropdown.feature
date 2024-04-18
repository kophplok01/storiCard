@dropdown-selection

Feature: Dropdown Selection

  @dropdown-options
  Scenario Outline: user can choose between the multiple option that the dropdown has
    Given the user is able to open the "chrome" browser on "<desktop>" resolution in "dev" environment
    When the user selects the "<option>" option from the example dropdown
    Then the option selected is "<option>"

    Examples:
      | option  |
      | Option1 |
      | Option2 |
      | Option3 |