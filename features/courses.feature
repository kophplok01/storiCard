@courses
Feature: Course Pricing Information

  @courses-by-price
  Scenario Outline: Print information for courses
    Given the user is able to open the "chrome" browser on "mobile" resolution in "dev" environment
    Then the user can print the number of courses priced at "<price>"

     Examples:
      | price  |
      | 25     |
      | 15     |