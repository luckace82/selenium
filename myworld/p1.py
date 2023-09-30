import os
from selenium import webdriver

chrome_path = "/usr/bin/google-chrome"  # Replace with the actual path to your Chrome binary

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_path

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com")
