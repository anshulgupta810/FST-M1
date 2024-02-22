# Set up the Firefox Driver with WebDriverManger
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

service = FirefoxService(GeckoDriverManager().install())

# Start the Driver
with webdriver.Firefox(service=service) as driver:
    # Navigate to the URL
    driver.get("https://alchemy.hguy.co/lms")

    # Print the title of the page
    print("Page title:- ", driver.title)
    Actual_title = driver.title
    Expected_title = "Alchemy LMS – An LMS Application"

    # Print the title of the new page
    print("New page title i:- ", driver.title)
    assert Actual_title == Expected_title, "Title mismatch"
    FirstInfoBox = driver.find_element(By.XPATH, "//h3[@class='uagb-ifb-title' and text()=' Actionable Training ']")
    ExpectedHeading = "Actionable Training"
    print("New heading is:- ", FirstInfoBox.text)
    assert FirstInfoBox.text == ExpectedHeading, "Heading mismatch"

    driver.quit()
