"""
@author 'Maksym Krutskykh'
@email 'maximkrut@yahoo.com'
@github 'https://gist.github.com/MaksymKrut'
"""
import configparser

from behave import *
import time as time


@when("I click on {element} element on {page} page")
def step_impl(context, element, page):
    locator = get_value_from_ini_file("locators", page, element)
    context.browser.implicitly_wait(10)
    context.browser.find_element_by_css_selector(locator).click()


@then("I should see {element} element on {page} page")
def step_impl(context, element, page):
    locator = get_value_from_ini_file("locators", page, element)
    context.browser.implicitly_wait(10)
    context.browser.find_element_by_css_selector(locator)


@when("I fill {field_locator} field on {page} page with {text}")
def step_impl(context, field_locator, page, text):
    field = get_value_from_ini_file("locators", page, field_locator)
    context.browser.find_element_by_css_selector(field).send_keys(text)


@then("I should see {text} text")
def step_impl(context, text):
    page = context.browser.page_source
    plain = page.encode('ascii', 'ignore')
    if text not in plain:
        print ("\n\nTest" + plain + "\n\nTest")
        raise Exception('Was not found!')


@then("I wait for {amount} seconds")
def step_impl(amount):
    assert isinstance(amount, float)
    time.sleep(amount)


def get_value_from_ini_file(file_name, section_header, key):
    config = configparser.ConfigParser()
    config.read("support/" + file_name + ".ini")
    value = config[section_header][key]
    return value


def get_page_element_by_css(context, page_name, locator_name):
    locator = get_value_from_ini_file("locators", page_name, locator_name)
    context.browser.implicitly_wait(10)
    element = context.browser.find_element_by_css_selector(locator)
    return element


def get_page_element_by_name(context, page_name, locator_name):
    locator = get_value_from_ini_file("locators", page_name, locator_name)
    context.browser.implicitly_wait(10)
    element = context.browser.find_element_by_name(locator)
    return element

