from playwright.sync_api import sync_playwright

def run():
    url = "https://demo.automationtesting.in/Register.html"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)

       
        country = page.locator('select#country')
        

        
        dob = page.locator('input[placeholder="Date of Birth"]')
        password = page.locator('input[ng-model="FirstName"]')  # adjust if needed
        confirm_password = page.locator('input[aria-label="Confirm Password"]')
        submit = page.locator('button[type="submit"]')

        
        country.select_option("India")
        dob.fill("01/01/1990")
        # Password fields may have specific selectors
        password.fill("Password123!")
        confirm_password.fill("Password123!")

        submit.click()

        # Optional: wait for success indicator
        page.wait_for_selector("text=Registration Successful", timeout=10000)

        page.wait_for_timeout(3000)
        browser.close()

if __name__ == "__main__":
    run()