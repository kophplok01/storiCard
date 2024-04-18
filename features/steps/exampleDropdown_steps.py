from behave import *


@when('the user selects the "{option}" option from the example dropdown')
def step_impl(context, option):
    context.home_page.example_dropdown_select_option(option)


@then('the option selected is "{option}"')
def step_impl(context, option):
    context.home_page.verify_dropdown_has_selected_option(option)