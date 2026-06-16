from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Open the seat reservation page
    page.goto('https://demoblaze.com/', wait_until='networkidle')

    #Sign up on the website
    page.locator('//a[@id="login2"]').click(froce=True)
    page.locator('//input[@id="loginusername"]').fill('ravi18')
    page.locator('//input[@id="loginpassword"]').fill('123456')
    page.locator('//button[text()="Log in"]').click()
    # Wait for the alert to appear and accept it
    page.wait_for_event('dialog').accept()

