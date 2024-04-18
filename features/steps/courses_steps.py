from behave import *


@then('the user can print the number of courses priced at "{price}"')
def step_impl(context, price):
    context.home_page.print_courses_by_price(price)
