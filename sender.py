from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

chrome_options = Options()
chrome_options.add_argument(r"--user-data-dir=C:\selenium-linkedin-profile")

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.get("https://www.linkedin.com")
time.sleep(5)

# -----------------------------
# Read message links
# -----------------------------
with open("thread_links.txt","r", encoding="utf-8") as f:
    message_links = [line.strip() for line in f if line.strip()]

# -----------------------------
# Read messages (multi-line)
# -----------------------------
with open("messages.txt","r",encoding="utf-8") as f:
    messages = f.read().split("===")

messages = [m.strip() for m in messages if m.strip()]
print("Loaded Messages:", messages)

# -----------------------------
# Send Messages
# -----------------------------
for link in message_links:

    driver.get(link)

    try:
        message_box = WebDriverWait(driver,20).until(
            EC.element_to_be_clickable((By.XPATH,"//div[@role='textbox']"))
        )

        message_box.click()

        # pick random message
        message_text = random.choice(messages)

        print("Sending:", message_text)

        message_box.send_keys(message_text)

        # send message
        message_box.send_keys(Keys.CONTROL, Keys.RETURN)

        print("Message Sent Successfully")

    except Exception as e:
        print("Failed:", e)

    # random delay to avoid LinkedIn detection
    time.sleep(random.randint(6,12))

print("All messages processed")