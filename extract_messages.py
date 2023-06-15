from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
import time


# Configure Chrome options to run in headless mode (no GUI)
chrome_options = Options()
# chrome_options.add_argument("--headless")

# Provide the path to your Chrome driver executable
# service = Service()

# service = Service(executable = "~/Users/anandtyagi/Downloads/chromedriver_mac_arm64/chromedriver.exe")
# service.service_url = "~/Users/anandtyagi/Downloads/chromedriver_mac_arm64/chromedriver.exe"
# chrome_driver_path = Service(executable_path="~/Users/anandtyagi/Downloads/chromedriver_mac_arm64/chromedriver.exe")
# chrome_driver_path = service.service_url
# Initialize the Chrome browser instance
driver = webdriver.Chrome(options=chrome_options)

# Open Google Messages web
driver.get("https://messages.google.com/web/conversations/687")

# Wait for the user to log in and load the messages
# Adjust the sleep duration based on the loading time of the messages

time.sleep(20)
# Find the chat conversation element
# chat_conversation = driver.find_element("class name", "bottom-anchored-scroll-pad")
chat_conversation = driver.find_element(By.CLASS_NAME, "content")

last_height = driver.execute_script("return document.getElementsByTagName('mws-bottom-anchored')[0].scrollHeight")
print(last_height)
# Scroll to the top of the chat conversation
while True:
    driver.execute_script("document.getElementsByTagName('mws-bottom-anchored')[0].scrollBy(0,-100000)")

    # Wait to load the page.
    time.sleep(5)

    # # Calculate new scroll height and compare with last scroll height.
    new_height = driver.execute_script("return document.getElementsByTagName('mws-bottom-anchored')[0].scrollHeight")
    print(new_height)
    # break when msg-id="1"

# print(message)
# # Extract the text messages from the chat conversation
# messages = driver.find_element("class name", "text-msg ng-star-inserted")
#
# for message in messages:
#     print(message.text)

# Close the browser
driver.quit()
