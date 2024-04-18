from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.home_page import HomePage
from read_properties import read_properties


@given('the user is able to open the "{browser}" browser on "{resolution}" resolution in "{environment}" environment')
def step_impl(context, browser, environment, resolution):
    if browser == "chrome":
        if resolution == "mobile":
            chrome_options = Options()
            chrome_options.add_argument(
                "--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36")
            chrome_options.add_argument("--window-size=375,812")
            context.driver = webdriver.Chrome(options=chrome_options)
        else:
            context.driver = webdriver.Chrome()
    elif browser == "firefox":
        if resolution == "mobile":
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.add_argument("--width=375")
            firefox_options.add_argument("--height=812")
            context.driver = webdriver.Firefox(options=firefox_options)
        else:
            context.driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    context.home_page = HomePage(context.driver, environment)
    context.home_page.load()


@then('the user is logged in as a "{username}"')
def step_impl(context, username):
    email, password = read_properties("users.properties", username)
    context.home_page.home_page_is_displayed()
    context.home_page.enter_credentials(email, password)



