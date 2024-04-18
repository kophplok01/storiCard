from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@fixture
def browser_driver(context):
    if context.config.userdata.get("browser") == "chrome":
        context.driver = webdriver.Chrome()
    elif context.config.userdata.get("browser") == "firefox":
        context.driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser")

    yield context.driver
    context.driver.quit()


def before_tag(context, tag):
    if tag == "fixture.browser":
        use_fixture(browser_driver, context)


def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()
