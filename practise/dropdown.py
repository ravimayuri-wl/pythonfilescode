from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://demo.automationtesting.in/Register.html", wait_until='networkidle')

    skills_dropdown = page.locator('//select[@id="Skills"]')
    skills_dropdown.select_option('Java')

    Year_dropdown = page.locator('//select[@id="yearbox"]')
    Year_dropdown.select_option('1990')

    Month_dropdown = page.locator('//select[@placeholder="Month"]')
    Month_dropdown.select_option('April')

    Day_dropdown = page.locator('//select[@id="daybox"]')
    Day_dropdown.select_option('15')


    page.wait_for_timeout(10000)
