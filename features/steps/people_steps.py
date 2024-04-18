from behave import *


@then('the user is able to print all the "{position}" names')
def step_impl(context, position):
    context.home_page.print_people_info_by_position(position)