from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1 * 1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://github.com/login')

    # Interact with login form
    page.get_by_label("Username or email address").fill("username")
    page.get_by_label("Password").fill("password")
    # page.get_by_role("button", name="Sign in").click()
    page.click('//*[@id="login"]/div[4]/form/div/input[13]')
    # Continue with the test

    # https://playwright.dev/python/docs/next/auth
    storage = context.storage_state(path="state.json")
    print('ok')


with sync_playwright() as playwright:
    run(playwright)
