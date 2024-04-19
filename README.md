# storiCard Challenge

The main flows for automated testing are UI testing, which are based on Selenium.

## Installation

To set up the repository and use it for testing on your local machine, please follow these guidelines. Ensure the following is installed:

- Python 3.12.3
- pip
- PyCharm IDE
- Selenium
- Behave
- Allure

```bash
pip install selenium
```

```bash
pip install behave
```

```bash
pip install allure-behave
```

## How to Run Examples

To run all test cases located in the feature folder, use the following command:

```bash
behave -f allure_behave.formatter:AllureFormatter -o reports/
```

To run only a specific case/feature, use a tag by adding 'features -t tagName' at the end of the command:

```bash
behave -f allure_behave.formatter:AllureFormatter -o reports/ features -t people-info  
```

After running that command, the execution report in JSON format will be generated and saved in a folder called `results`. To view the HTML version, run:

```bash
allure serve reports
```
## Structure of Scenarios
In this example, the scenario outline allows for changing parameters such as browser type (`chrome` or `firefox`), 
resolution (`desktop` or `mobile`), and environment (`dev`, `acc`, or `qa`) to cover various testing scenarios. This flexibility enables comprehensive testing across different configurations and environments.
```gherkin
Feature: Home page for visitors and users

  @home-page
  Scenario Outline: User is able to login and logout using different configurations
    Given the user is able to open the "<browser>" browser on "<resolution>" resolution in "<environment>" environment
    Then the user is logged in as a "devTestUser1"

    Examples:
      | browser | resolution | environment |
      | chrome  | desktop    | dev         |
      | firefox | desktop    | acc         |
      | chrome  | mobile     | qa          |
      | firefox | mobile     | dev         |
  ```  
## Usage of Tags

Tags can be used to run specific test cases or features. Use the `-t` flag followed by the tag name to run tests with specific tags. For example:

```bash
behave -f allure_behave.formatter:AllureFormatter -o reports/ features -t home-page
```

## About Allure

Allure is a tool for test reporting that generates interactive and comprehensive reports. It provides insights into test execution, including statistics, trends, and graphs.

## Generating XML Reports with JUnit
If you need to generate XML reports compatible with JUnit for integration with other testing tools or systems, you can use the following command:
```bash
behave -f junit --junit
```
This command will generate XML reports in the `reports` directory, which can then be used for further analysis or integration with CI/CD pipelines.


## Troubleshooting

If you encounter any issues during installation or execution, refer to the following troubleshooting tips:

- **Issue**: Missing dependencies
  **Solution**: Ensure all required dependencies are installed as per the installation instructions.

- **Issue**: Command not recognized
  **Solution**: Double-check the command syntax and ensure all required flags are included.

- **Issue**: Test failures
  **Solution**: Check test logs and error messages for clues on why the tests are failing. Review test code and ensure it's functioning as expected.
