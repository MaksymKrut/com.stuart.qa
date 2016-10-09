# coding=utf-8
"""
@author 'Maksym Krutskykh'
@email 'maximkrut@yahoo.com'
@github 'https://gist.github.com/MaksymKrut'
"""
from common import *
from selenium.webdriver.common.keys import Keys


@given("I am on the home page")
def step_impl(context):
    url = get_value_from_ini_file("config", "Base", "home url")
    context.browser.get(url)


@when("I login as {user_type} user")
def step_impl(context, user_type):
    email = get_value_from_ini_file("config", user_type + " User", "email")
    password = get_value_from_ini_file("config", user_type + " User", "password")
    get_page_element_by_css(context, "Login", "email field").clear()
    get_page_element_by_css(context, "Login", "password field").clear()
    get_page_element_by_css(context, "Login", "email field").send_keys(email)
    get_page_element_by_css(context, "Login", "password field").send_keys(password)
    get_page_element_by_css(context, "Login", "login button").click()


@when("I fill in pick up form")
def step_impl(context):
    get_page_element_by_name(context, "Order", "pu first name field").send_keys("Vincent")
    get_page_element_by_name(context, "Order", "pu last name field").send_keys("Vega")
    get_page_element_by_name(context, "Order", "pu company field").send_keys("Pulp Fiction")
    address_field = get_page_element_by_name(context, "Order", "pu address field")
    address_field.clear()
    address_field.send_keys("Carrer de Balmes, 88, Barcelona, Spain")
    time.sleep(1)
    address_field.send_keys(Keys.ENTER)
    time.sleep(1)
    get_page_element_by_name(context, "Order", "pu phone field").send_keys("+34666666666")
    get_page_element_by_name(context, "Order", "pu email field").send_keys("be_f_cool_email@stuart.com")
    get_page_element_by_name(context, "Order", "pu comment field").send_keys("test")


@then("I fill in drop off form")
def step_impl(context):
    get_page_element_by_css(context, "Order", "do first name field").send_keys("Marsellus")
    get_page_element_by_css(context, "Order", "do last name field").send_keys("Walles")
    get_page_element_by_css(context, "Order", "do company field").send_keys("Pulp Fiction")
    address_field = get_page_element_by_css(context, "Order", "do address field")
    address_field.clear()
    address_field.send_keys("Carrer de Tarragona 141")
    time.sleep(1)
    address_field.send_keys(Keys.ENTER)
    time.sleep(1)
    get_page_element_by_css(context, "Order", "do phone field").send_keys("+34666666667")
    get_page_element_by_css(context, "Order", "do email field").send_keys("be_f_cool_email@stuart.com")
    get_page_element_by_css(context, "Order", "do comment field").send_keys("test")

