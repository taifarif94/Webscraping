from selenium import webdriver
from bs4 import BeautifulSoup
import os
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time  # Import the time module

# Get the current script's directory and path to geckodriver
current_directory = os.path.dirname(os.path.realpath(__file__))
geckodriver_path = os.path.join(current_directory, 'geckodriver.exe')

# Initialize the WebDriver for Firefox
driver = webdriver.Firefox(executable_path=geckodriver_path)

# URL of the first page to scrape
# Placeholder for website
first_page_url = 'https://somewebsite.com'

# Open the first page
driver.get(first_page_url)

# Wait for login and manual navigation to the correct page if needed
input("Press Enter after logging in and ensuring you are on the correct page...")

# Prepare to write to a CSV file
with open('Words.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Word'])  # Writing header

    for page in range(1, 100):  # Loop through 99 pages
        print(f"Processing page {page}...")
        url = f'https://somewebsite.com/{page}'
        driver.get(url)
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, "div.text.css-1cluisu"))
        # )
        input("Press Enter if page is loaded!")
        time.sleep(1)  # Wait for 1 seconds before scraping
        # Extract words after the page loads
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        words = soup.find_all('div', class_='text css-1cluisu')

        for word in words:
            print(word.text.strip())
            writer.writerow([word.text.strip()])

# Close the browser
driver.quit()

print("Data extraction complete and saved to Words.csv.")
