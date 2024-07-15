from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from database_parks import update_database_parks  # Import database function

def metservice_scrape(url):
    browser_driver = Service('/usr/lib/chromium-browser/chromedriver')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--remote-debugging-port=9222')

    driver = webdriver.Chrome(service=browser_driver, options=chrome_options) 
    try:
        # Navigate to the webpage
        driver.get('https://www.metservice.com/mountains-and-parks/national-parks/' + url)

        # Extract the page source HTML
        html = driver.page_source

        # Parse the HTML with BeautifulSoup using the 'html.parser'
        soup = BeautifulSoup(html, 'html.parser')

        # Find Title
        title_elements = soup.find_all(class_="Tile-body-header")
        title = title_elements[0].text.strip() if title_elements else "No title element found."
        

        # Find Date
        date_elements = soup.find_all(class_="u-textRegular u-pL-xs")
        today_date = date_elements[0].text.strip() if date_elements else "Today date not found."
        tomorrow_date = date_elements[1].text.strip() if len(date_elements) > 1 else "Tomorrow date not found."

        # Find Overview
        overview_elements = soup.find_all(class_="u-mT-0 u-mT-xs")
        today_overview = overview_elements[0].text.strip() if overview_elements else "Today overview not found."
        tomorrow_overview = overview_elements[1].text.strip() if len(overview_elements) > 1 else "Tomorrow overview not found."

        # Find Mountain Weather Hazards
        weather_elements = soup.find_all(class_="u-textSemibold")
        today_weather_hazards = weather_elements[0].text.strip() if weather_elements else "Today weather hazards not found."
        tomorrow_weather_hazards = weather_elements[1].text.strip() if len(weather_elements) > 1 else "Tomorrow weather hazards not found."

        # Find Issue Time
        issue_elements = soup.find_all(class_="fineprint u-block u-textGrey u-mT-xs")
        today_issue_time = issue_elements[0].text.strip() if issue_elements else "Today issue time not found."
        tomorrow_issue_time = issue_elements[1].text.strip() if len(issue_elements) > 1 else "Tomorrow issue time not found."

        # Insert data into the database
        data = (title, today_date, tomorrow_date, today_overview, tomorrow_overview,
                today_weather_hazards, tomorrow_weather_hazards, today_issue_time, tomorrow_issue_time)
        
        update_database_parks(data)

    finally:
        # Close the browser
        driver.quit()

    return()
