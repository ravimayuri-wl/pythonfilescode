from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    page.goto("https://www.demoblaze.com/")
    page.locator('//a[@id="login2"]').click()
    page.locator('//input[@id="loginusername"]').fill("ravi")
    page.locator('//input[@id="loginpassword"]').fill("123456")
    page.locator('//button[@onclick="logIn()"]').click(force=True)
    page.wait_for_timeout(10000)

    
    page.goto("https://demoblaze.com/prod.html?idp_=1")
    page.locator('//button[@onclick="addToCart(1)"]').click(force=True)

    page.locator('//a[@id="cartur"]').click()
    