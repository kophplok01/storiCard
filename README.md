# storiCard Challenge. 
The main flows for automated testing are UI testing, the UI tests are based on selenium.

## Installation
For setting up repository and using it for testing on your local machine, please first follow the following guidelines.
Following should be installed.
* python 3.12.3
* pip
* pycharm IDE
* selenium
* behave 
* allure 
```bash
pip install selenium
```
```bash
pip install behave
```
```bash
install allure-behave
```

## how to run example

the following command can be used to run all the test cases located in the feature folder
```bash
behave -f allure_behave.formatter:AllureFormatter -o reports/
```
If it is required to run only one specific case/feature, a tag can be used by adding 'features -t tagName' at the end of the command.
```bash
behave --f allure_behave.formatter:AllureFormatter -o results/ features -t people-info  
```

After run that command the execution report in JSON format will be generated and saved in a folder called 'results'
to see the html version of it run the following command
```bash
allure serve results  
```
