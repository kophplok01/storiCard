from behave import *


@when('the user clicks the "Open Window" button')
def step_impl(context):
    context.home_page.click_open_window_button()


@then("the user should be able to see the expected text")
def step_impl(context):
    context.home_page.find_element_in_new_window("30 day money back guarantee")
