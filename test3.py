import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):

    print("before the test runs")

    # Go to the starting url before each test.
    page.goto("https://playwright.dev/")
    yield

    print("after the test runs")


def test_do_stuff(page: Page):    
    #page.get_by_label("Main", exact=True).get_by_role("link", name="Python").click()
    page.get_by_role("link", name="Get started").click()
    page.get_by_role("link", name="Next Writing tests »").click()
    page.get_by_role("link", name="Next Running tests »").click()
    page.get_by_role("link", name="Next Test generator »").click()
    page.get_by_role("link", name="Test Generator", exact=True).click()
    # page.get_by_role("tab", name="Async").click()
    # page.get_by_role("tab", name="Sync", exact=True).click()
    # page.get_by_role("tab", name="Async").click()


