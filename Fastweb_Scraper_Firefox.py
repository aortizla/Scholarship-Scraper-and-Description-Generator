import csv
import re
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

# Set up the Selenium driver
service = Service(GeckoDriverManager().install())
options = webdriver.FirefoxOptions()
options.headless = True  # Set to False if you want to see the browser window
driver = webdriver.Firefox(service=service, options=options)

# Navigate to the website
url = "https://www.fastweb.com/college-scholarships/scholarships?filter=Matched"
driver.get(url)

# Ask for login credentials
username = input("Enter your username: ")
password = input("Enter your password: ")

# Find the username and password input fields
username_field = driver.find_element("id", "login_email")
password_field = driver.find_element("id", "user_password")

# Enter the login credentials
username_field.send_keys(username)
password_field.send_keys(password)

# Submit the login form (adjust this line based on the login button's HTML element)
login_button = driver.find_element("id", "user_form_submit")
login_button.click()

# Wait for the page to load after login (adjust the time if needed)
time.sleep(10)

# Initialize lists to store the data
view_links = []
deadlines = []
awards = []

# Keep scrolling and clicking the "Next" button until there's no more data
while True:
    # Get the page source
    html = driver.page_source

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all scholarship rows
    scholarship_rows = soup.find_all('tbody', id=lambda x: x and x.startswith('scholarship_'))

    # Extract data from each scholarship row
    for row in scholarship_rows:
        # Find the "View" button link
        view_button = row.find('a', class_='active_award')
        link = view_button.get('href') if view_button else None
        if link:
            view_links.append(f"https://www.fastweb.com{link}")
        else:
            view_links.append('')

        # Find the deadline and award information
        info_cells = row.find_all('td', class_='info')
        if len(info_cells) >= 2:
            deadlines.append(info_cells[0].get_text(strip=True))
            awards.append(info_cells[1].get_text(strip=True))
        else:
            deadlines.append('')
            awards.append('')

    # Try to find the "Next" button
    next_button = driver.find_elements(by="xpath", value="//a[@rel='next']")

    if next_button:
        # Scroll to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Click the "Next" button
        next_button[0].click()

        # Wait for the page to load (adjust the time if needed)
        time.sleep(5)

    else:
        # No more "Next" button, break the loop
        break

# Define the CSV filename
csv_filename = "scholarship_links.csv"

# Write the data to a CSV file
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['View Link', 'Award', 'Deadline'])
    for i in range(len(view_links)):
        writer.writerow([view_links[i], deadlines[i], awards[i]])

print(f"Scholarship data scraped successfully and saved to {csv_filename}")

# Close the Selenium driver
driver.quit()