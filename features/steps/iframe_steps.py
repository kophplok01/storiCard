from behave import *


@when("I switch to the iframe")
def step_impl(context):
    context.home_page.switch_to_courses_iframe()


@step("the user search for an specific text")
def step_impl(context):
    context.home_page.print_odd_elements_in_iframe()
