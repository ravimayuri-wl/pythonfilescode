from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://uncodemy.com/", wait_until='networkidle')

#mouse hover
    page.locator(' //*[@id="categoriesBtn"]').click()
    page.locator(' //*[@id="categoriesBtn"]').click()
   /html/body/nav/div[2]/div[1]/nav/menu/menuitem/menu/menuitem[1]/a


    page.locator('//a[text()="Python"]').click()
    

    
    page.wait_for_timeout(10000)
