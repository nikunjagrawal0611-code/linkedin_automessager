from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# -----------------------------
# Use your logged-in Chrome profile
# -----------------------------
chrome_options = Options()
chrome_options.add_argument(r"--user-data-dir=C:\selenium-linkedin-profile")

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# -----------------------------
# Open messaging page
# -----------------------------
driver.get("https://www.linkedin.com/messaging/")

time.sleep(7)

# -----------------------------
# Scroll to load more chats
# -----------------------------
for i in range(8):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# -----------------------------
# Find conversation list
# -----------------------------
threads = driver.find_elements(By.XPATH, "//li[contains(@class,'msg-conversation-listitem')]")

links = []

for thread in threads:

    try:
        thread.click()
        time.sleep(3)

        # copy URL after opening chat
        current_link = driver.current_url

        if current_link not in links:
            links.append(current_link)
            print("Saved:", current_link)

    except:
        pass

# -----------------------------
# Save links
# -----------------------------
with open("thread_links.txt","w") as f:
    for link in links:
        f.write(link + "\n")

print("Total links:", len(links))

driver.quit()