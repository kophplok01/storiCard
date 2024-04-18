@people
Feature: Print Names from Fixed Header Web Table

  @people-info
  Scenario Outline: Print names of all people by his position
    Given the user is able to open the "chrome" browser on "mobile" resolution in "dev" environment
    Then the user is able to print all the "<position>" names

    Examples:
      | position    |
      | Engineer    |
      | Businessman |