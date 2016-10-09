"""
@author 'Maksym Krutskykh'
@email 'maximkrut@yahoo.com'
@github 'https://gist.github.com/MaksymKrut'
"""

from selenium import webdriver


def before_all(context):
    context.browser = webdriver.Firefox()
    context.browser.maximize_window()
    context.browser.implicitly_wait(10)


def after_all(context):
    context.browser.quit()
