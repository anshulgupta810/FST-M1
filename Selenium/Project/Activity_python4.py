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
    SecondInfoBox = driver.find_element(By.XPATH, "//div[@class='ld_course_grid_price free']//following-sibling::div[@class='caption']/h3[text()='Email Marketing Strategies']")
    ExpectedHeading = "Email Marketing Strategies"
    print("New heading is:- ", SecondInfoBox.text)
    assert SecondInfoBox.text == ExpectedHeading, "Heading mismatch"

    driver.quit()
