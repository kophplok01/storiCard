@testing-suggestion-input

Feature: Testing Suggestion Input

  @less-than-two-letters
  Scenario: No suggestions are displayed when typing less than two letters
    Given the user is able to open the "chrome" browser on "mobile" resolution in "dev" environment
    When the user type "U" into the suggestion input
    Then the user should not see any suggestions

  @at-least-two-letters
  Scenario: Suggestions are displayed when typing at least two letters
    Given the user is able to open the "chrome" browser on "desktop" resolution in "dev" environment
    When the user type "Un" into the suggestion input
    Then the user should see a list of suggestions

  @filtered-suggestions
  Scenario Outline: Suggestions are filtered based on input
    Given the user is able to open the "chrome" browser on "<desktop>" resolution in "dev" environment
    When the user type "Un" into the suggestion input
    Then the user should see suggestions containing "<country>"

    Examples:
      | country             |
      | United States (USA) |
      | United Kingdom (UK) |

  @selecting-suggestion
  Scenario: Selecting a suggestion
    Given the user is able to open the "chrome" browser on "<desktop>" resolution in "dev" environment
    When the user type "Un" into the suggestion input
    And the user select "United States" from the suggestions
    Then the suggestion input should contain "United States"

  @clearing-input-field
  Scenario: Clearing the input field
    Given the user is able to open the "chrome" browser on "<desktop>" resolution in "dev" environment
    When the user type "Un" into the suggestion input
    And the user clear the suggestion input
    Then the suggestion input should be empty

  @handling-special-characters
  Scenario: Handling special characters
    Given the user is able to open the "chrome" browser on "<desktop>" resolution in "dev" environment
    When the user type special characters into the suggestion input
    Then the user should not see any suggestions
