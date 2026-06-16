from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("http://tdfuji28s.sys.meshcore.net:13500/ibogui/cc/login", wait_until='networkidle')
    page.locator('//input[@id="email"]').fill("admin")
    page.locator('//input[@id="password"]').fill("test123")
    #page.locator('//input[@id="password"]').press("Enter")
        
    page.locator('//*[@id="btSubmit"]').click(force=True)
    
    page.wait_for_timeout(10000)

    
