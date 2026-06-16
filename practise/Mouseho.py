from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://demo.automationtesting.in/Register.html", wait_until='networkidle')
    page.wait_for_timeout(1000)

    Fname = page.locator('//input[@placeholder="First Name"]').fill("Ravi")
    Lname = page.locator('//input[@placeholder="Last Name"]').fill("Kumar")
    Address = page.locator('//textarea[@ng-model="Adress"]').fill("Pune, Maharashtra")
    email = page.locator('//input[@type="email"]').fill("ravim@gmail.com")
    phone = page.locator('//input[@type="tel"]').fill("9876543210")
    gender = page.locator('//input[@value="Male"]').check()
    Hobbies = page.locator("//input[@value='Cricket']").check()

    
    #page.locator('//*[@id="countries"]').set_focus()
    
    skills_dropdown = page.locator('//select[@id="Skills"]')
    skills_dropdown.select_option('Java')

    page.wait_for_timeout(3000)
    page.locator("//span[@role='combobox']").click().locator("//input[@type='search']").fill("India").press("Enter")


    page.locator("//label[text()='Country']").click()
    page.wait_for_timeout(1000)
  
    country = page.locator('select#country')
    country.select_option("India")

    Year_dropdown = page.locator('//select[@id="yearbox"]')
    Year_dropdown.select_option('1990')

    Month_dropdown = page.locator('//select[@placeholder="Month"]')
    Month_dropdown.select_option('April')

    Day_dropdown = page.locator('//select[@id="daybox"]')
    Day_dropdown.select_option('15')

    page.locator("//input[@id='firstpassword']").fill("test123")
    page.locator("//input[@id='secondpassword']").fill("test123")

    page.locator("//div[@id='msdd']").click()
    page.locator("//a[text()='English']").click()
    page.locator("//a[text()='Hindi']").click()
    page.locator("//div[@id='msdd']").click()

    page.wait_for_timeout(10000)
