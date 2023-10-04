from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://playwright.dev/")
    page.get_by_label("Main", exact=True).get_by_role("link", name="Python").click()
    page.get_by_role("link", name="Get started").click()
    page.get_by_role("link", name="Next Writing tests »").click()
    page.get_by_role("link", name="Next Running tests »").click()
    page.get_by_role("link", name="Next Test generator »").click()
    page.get_by_role("link", name="Test Generator", exact=True).click()
    page.get_by_role("tab", name="Async").click()
    page.get_by_role("tab", name="Sync", exact=True).click()
    page.get_by_role("tab", name="Async").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
