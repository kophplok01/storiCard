from behave import *


@then("the user prints the text in the alert and clicks on OK")
def step_impl(context):
    context.home_page.print_alert_text()


@when('the user types "{text}" and clicks the "{type}" button')
def step_impl(context, text, type):
    context.home_page.input_text_for_dialog(text, type)


@then("the user prints the text in the confirm alert")
def step_impl(context):
    context.home_page.print_alert_text()


@step('the user confirms that the alert text is equal to "{expected_text}" and then click ok')
def step_impl(context,expected_text):
    context.home_page.expected_text_for_dialog(expected_text)
