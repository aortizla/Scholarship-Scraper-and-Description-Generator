Scholarship Scraper and Description Generator

This repository contains Python scripts to scrape scholarship data from a website and generate descriptions for each scholarship.
Overview

The project consists of three main scripts:

    Step One/Code One: This script scrapes scholarship data from the website fastweb.com, including view links, awards, and deadlines. It saves the data to a CSV file named scholarship_links.csv.

    Step Two/Code Two: This script reads the CSV file generated in step one, cleans the data by removing duplicate links and rows with missing values, and saves the cleaned data to a new CSV file named scholarship_links_cleaned.csv.

    Step Three/Code Three: This script reads the cleaned CSV file, retrieves scholarship descriptions by visiting each scholarship's URL, and generates a Word document (scholarship_descriptions.docx) containing the scholarship URLs, awards, deadlines, and descriptions.

Requirements

    Python 3.x
    Libraries: csv, re, selenium, webdriver_manager, bs4, time, pandas, requests, docx

Installation

    Clone this repository to your local machine:
    
    git clone https://github.com/Coding-Journey-2004/Scholarship-Scraper-and-Description-Generator.git

Install the required Python libraries:

    pip install -r requirements.txt

Usage

    Step One/Code One:
        Run the script Fastweb_ScraperFirefox/Chrome.py
        Enter your Fastweb username and password when prompted.
        Wait for the script to scrape scholarship data. The data will be saved to scholarship_links.csv.

    Step Two/Code Two:
        Run the script data_cleanup.py
        This script will clean the data in scholarship_links.csv and save the cleaned data to scholarship_links_cleaned.csv.

    Step Three/Code Three:
        Run the script automated_description_docx.py
        This script will generate scholarship descriptions by visiting each URL in scholarship_links_cleaned.csv and save the descriptions to a Word document named scholarship_descriptions.docx.

Notes

    Ensure that you have a stable internet connection while running the scripts, especially Step One/Code One and Step Three/Code Three, as they require web scraping.

    Adjustments may be needed in the scripts based on changes to the website's structure or login process.

    Make sure to provide appropriate permissions for file read and write operations.

    Use the scripts responsibly and adhere to the website's terms of service.

    For any issues or improvements, feel free to submit a pull request or open an issue in the repository.

Happy scraping! 🌟