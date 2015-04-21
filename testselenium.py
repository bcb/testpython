"""common.py"""
#pylint:disable=unused-wildcard-import

import re
import time

from behave import * #pylint:disable=wildcard-import


def assert_uri(context, string):
    """Ensure the uri is correct"""
    time.sleep(1)
    assert re.search(string, context.browser.current_url)


def assert_heading(context, string):
    """Ensure the heading is correct"""
    assert context.browser.find_elements_by_xpath(
        '//h1[@id="page_heading" and contains(., "'+string+'")]')[0] \
        .is_displayed()


def assert_title(context, string):
    """Ensure the title is correct"""
    assert re.search(string, context.browser.title)


@then('I should see the message "{text}"')
@then('I should see "{text}"')
def step_impl(context, text):
    """Checks a flash message or other text in the page"""
    time.sleep(1)
    assert text in context.browser.page_source
