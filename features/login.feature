@home-page
Feature: Home page for visitors and users

  @home-page-desktop
  Scenario Outline: User is able to login and logout in different browsers on desktop resolution
    Given the user is able to open the "<browser>" browser on "<desktop>" resolution in "dev" environment
    Then the user is logged in as a "devTestUser1"

    Examples:
      | browser |
      | chrome  |
      | firefox |

  @home-page-mobile
  Scenario Outline: User is able to login and logout in different browsers on mobile resolution
    Given the user is able to open the "<browser>" browser on "mobile" resolution in "dev" environment
    Then the user is logged in as a "devTestUser1"

    Examples:
      | browser |
      | chrome  |
      | firefox |


