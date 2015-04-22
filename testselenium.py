"""common.py"""
#pylint:disable=unused-wildcard-import

import re
from time import sleep

from behave import * #pylint:disable=wildcard-import


def assert_uri(context, string):
    """Ensure the uri is correct"""
    sleep(0.5)
    assert re.search(string, context.browser.current_url)


def assert_heading(context, string):
    """Ensure the heading is correct"""
    assert context.browser.find_elements_by_xpath(
        '//h1[@id="page_heading" and contains(., "'+string+'")]')[0] \
        .is_displayed()


def assert_title(context, string):
    """Ensure the title is correct"""
    sleep(0.5)
    assert re.search(string, context.browser.title)


# Given
@given('I\'ve not logged in')
def step_impl(context):
    context.browser.get('http://localhost/logout')


@given('I\'ve logged in')
def step_impl(context):
    context.browser.get('http://localhost/login')
    context.execute_steps('''
        When I login
    ''')


# When
@when('I visit the login page')
def step_impl(context):
    context.browser.get('http://localhost/login')


@when('I visit the logout page')
def step_impl(context):
    context.browser.get('http://localhost/logout')


@when('I login')
def step_impl(context):
    context.browser.find_element_by_xpath('//input[@name="username"]') \
        .send_keys('admin')
    context.browser.find_element_by_xpath('//input[@name="password"]') \
        .send_keys('pass')
    context.browser.find_element_by_xpath('//input[@name="submit"]').click()


@when('I attempt a failed login')
def step_impl(context):
    context.browser.find_element_by_xpath('//input[@name="username"]') \
        .send_keys('noname')
    context.browser.find_element_by_xpath('//input[@name="password"]') \
        .send_keys('nopass')
    context.browser.find_element_by_xpath('//input[@name="submit"]').click()


# Then
@then('I should see the login page')
def step_impl(context):
    assert_uri(context, '/login')
    assert_heading(context, 'Login')


@then('I should see the message "{text}"')
@then('I should see "{text}"')
def step_impl(context, text):
    """Checks a flash message or other text in the page"""
    sleep(0.5)
    assert text in context.browser.page_source
