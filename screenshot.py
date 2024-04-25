from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (useful for headless mode)

# Set the path to the ChromeDriver executable
chrome_driver_path = 'chromedriver.exe'

# Create a Chrome WebDriver instance with the configured options
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

class Screenshot:
    def __init__(self, driver, path):
        self.driver = driver
        self.path = path

    def take_screenshot(self, url):
        # Set the window size to a fixed value
        self.driver.set_window_size(1920, 1080)
        self.driver.get(url)
        
        # Wait for the body element to become available
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        
        # Capture the screenshot
        self.driver.save_screenshot(self.path + '/screenshot.png')

# Define the Screenshot class
screenshot = Screenshot(driver, './screenshots')
screenshot.take_screenshot('https://d3fend.mitre.org/')

# Close the WebDriver
driver.quit()
