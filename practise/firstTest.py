from playwright.sync_api import sync_playwright # Import the Playwright library for synchronous API
with sync_playwright() as p: # Launch the browser and navigate to Google
        browser = p.chromium.launch(headless=False) # Set headless to False to see the browser window
        page = browser.new_page() # Create a new page
        page.goto("https://b2o-worldline.azurewebsites.net/seatreservation") # Navigate to Google
        #page.screenshot(path="google.png") # Take a screenshot and save it as google.png
        #browser.close()