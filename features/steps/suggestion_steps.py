from behave import *


@when('the user type "{value}" into the suggestion input')
def step_impl(context, value):
    context.home_page.suggestion_input(value)


@then("the user should not see any suggestions")
def step_impl(context):
    context.home_page.suggestion_list_is_displayed(check_visibility=False)


@then("the user should see a list of suggestions")
def step_impl(context):
    context.home_page.suggestion_list_is_displayed()


@then('the user should see suggestions containing "{country}"')
def step_impl(context, country):
    context.home_page.suggestion_list_contains_expected_country(country=country)


@step('the user select "{country}" from the suggestions')
def step_impl(context, country):
    context.home_page.select_country_from_suggestions(country)


@then('the suggestion input should contain "{country}"')
def step_impl(context, country):
    context.home_page.verify_input_contains_selected_country(country)


@step("the user clear the suggestion input")
def step_impl(context):
    context.home_page.clear_input_field()


@then("the suggestion input should be empty")
def step_impl(context):
    context.home_page.verify_input_field_empty()


@when("the user type special characters into the suggestion input")
def step_impl(context):
    context.home_page.suggestion_input("#$%&")