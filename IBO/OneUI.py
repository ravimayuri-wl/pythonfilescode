from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("http://tdfuji28s.sys.meshcore.net:4212/dispute/", wait_until='networkidle')
    page.wait_for_timeout(1
    
    000)

    page.locator('//input[@id="username"]').fill("qauser_bcs")
    page.locator('//input[@id="password"]').fill("test123")
    #page.locator('//input[@id="password"]').press("Enter")
        
    page.locator('//*[@id="btSubmit"]').click(force=True)
    
    page.wait_for_timeout(10000)

    
