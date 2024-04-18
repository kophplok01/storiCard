from behave import *


@when('the user clicks the "Open tab" button')
def step_impl(context):
    context.home_page.click_open_tab_button()


@then("the user should be able to see the expected button")
def step_impl(context):
    context.home_page.verify_button_in_new_tab("Clicking a new tab Button and see the expected view")