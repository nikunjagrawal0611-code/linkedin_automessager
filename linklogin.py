from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument(r"--user-data-dir=C:\selenium-linkedin-profile")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com")

input("Login manually and press ENTER here when done...")