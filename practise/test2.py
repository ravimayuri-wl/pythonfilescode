from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Open the seat reservation page
    page.goto('https://b2o-worldline.azurewebsites.net/seatreservation', wait_until='networkidle')
