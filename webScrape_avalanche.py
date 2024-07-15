from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from database_avalanche import update_database_avalanche
import database_avalanche
# from database_parks import update_database_parks  # Import database function

def avalanche_advisory_scrape(region):
    start = time.time()
    browser_driver = Service('/usr/lib/chromium-browser/chromedriver')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--remote-debugging-port=9222')

    driver = webdriver.Chrome(service=browser_driver, options=chrome_options) 
 
    try:
        # Navigate to the webpage
        driver.get('https://www.avalanche.net.nz/region/'+region)

        # Extract the page source HTML
        html = driver.page_source

        # Parse the HTML with BeautifulSoup using the 'html.parser'
        soup = BeautifulSoup(html, 'html.parser')

        # Find Title
        elements = soup.find_all(class_="font-weight-bold")
        title = elements[0].text.strip() if elements else "No title element found."
        # print(title)

       

        # Find Overview
        overview = elements[1].text.strip() if elements else "No overview element found."
        # print(overview)
        
        # Find Issue Time
        times = soup.find_all(class_="col-12 col-print-6")
        issue_time = times[0].text.strip() if elements else "No issue time element found."
        # print(issue_time)

        # Find Valid Time
        valid_time = times[1].text.strip() if elements else "No valid element found."
        # print(valid_time)

        # Find Avalanche Risk
        risk_level = soup.find_all(class_="risk-pill__description")
        risk_level_overview = risk_level[0].text.strip() if risk_level else "Risk Level Overview not found."
        # print(risk_level_overview)

        # Find High Alpine        
        risk_level_high = risk_level[1].text.strip() if risk_level else "Risk Level High Alpine not found."
        # print(risk_level_high)

        risk_description = soup.find_all(class_="mb-0")
        risk_d_high = risk_description[1].text.strip() if risk_description else "Risk Description High Alpine not found."
        # print(risk_d_high)

        # Find Alpine        
        risk_level_alpine = risk_level[2].text.strip() if risk_level else "Risk Level Alpine not found."
        # print(risk_level_alpine)
        risk_d_alpine = risk_description[2].text.strip() if risk_description else "Risk Description Alpine not found."
        # print(risk_d_alpine)

        # Find Alpine        
        risk_level_sub = risk_level[3].text.strip() if risk_level else "Risk Level Sub Alpine not found."
        # print(risk_level_sub)
        risk_d_sub = risk_description[3].text.strip() if risk_description else "Risk Description Sub Alpine not found."
        # print(risk_d_sub)

        # Avalanche Problem 1
        avalanche_problem = soup.find_all('img')
        problem_1_img = avalanche_problem[13]
        problem_1 = problem_1_img.get('alt', "Avalanche Problem 1 not found.")
        # print(problem_1)
        risk_d_problem_1 = risk_description[4].text.strip() if risk_description else "Risk Description Problem not found."
        # print(risk_d_problem_1)
        risk_trend_1 = risk_description[5].text.strip() if risk_description else "Risk Trend not found."
        # print(risk_trend_1)
        risk_time_of_day = risk_description[6].text.strip() if risk_description else "Risk Time of Day not found."
        # print(risk_time_of_day)

        
        # Likelihood Problem 1
        likelihood_headings = soup.find_all('h3', class_='avalanche-danger-row__heading', string="Likelihood")
        # Check if the <h3> exists and find the gauge wrapper div
        likelihood_heading = likelihood_headings[0]
        if likelihood_heading:
            gauge_wrapper = likelihood_heading.find_next('div', class_='gauge__wrapper')
            if gauge_wrapper:
                # Find all gauge segments with the 'filled' class
                filled_gauges = gauge_wrapper.find_all('div', class_='gauge__segment--filled')
                total_gauges = gauge_wrapper.find_all('div', class_='gauge__segment')
                likelihood_problem1 = len(filled_gauges)
                # print(f"Likelihood: {likelihood_problem1} out of {len(total_gauges)}")


        # Size Problem 1
        size_headings = soup.find_all('h3', class_='avalanche-danger-row__heading', string="Size")
        # Check if the <h3> exists and find the gauge wrapper div
        size_heading = size_headings[0]
        if size_heading:
            gauge_wrapper = size_heading.find_next('div', class_='gauge__wrapper')
            if gauge_wrapper:
                # Find all gauge segments with the 'filled' class
                filled_gauges = gauge_wrapper.find_all('div', class_='gauge__segment--filled')
                total_gauges = gauge_wrapper.find_all('div', class_='gauge__segment')
                size_problem1 = len(filled_gauges)
                # print(f"Size: {size_problem1} out of {len(total_gauges)}")


        # Avalanche Problem 2
        problem_2_img = avalanche_problem[14]
        problem_2 = problem_2_img.get('alt', "Avalanche Problem 2 not found.")
        # print(problem_2)
        risk_d_problem_2 = risk_description[7].text.strip() if risk_description else "Risk Description Problem not found."
        # print(risk_d_problem_2)
        risk_trend_2 = risk_description[8].text.strip() if risk_description else "Risk Trend not found."
        # print(risk_trend_2)
        risk_time_of_day_2 = risk_description[9].text.strip() if risk_description else "Risk Time of Day not found."
        # print(risk_time_of_day_2)

        # Likelihood Problem 2
        likelihood_heading2 = likelihood_headings[1]
        if likelihood_heading2:
            gauge_wrapper2 = likelihood_heading.find_next('div', class_='gauge__wrapper')
            if gauge_wrapper2:
                # Find all gauge segments with the 'filled' class
                filled_gauges2 = gauge_wrapper2.find_all('div', class_='gauge__segment--filled')
                total_gauges2 = gauge_wrapper2.find_all('div', class_='gauge__segment')
                likelihood_problem2 = len(filled_gauges2)
                # print(f"Likelihood: {likelihood_problem2} out of {len(total_gauges2)}")


        # Size Problem 2
        size_heading2 = size_headings[1]
        if size_heading2:
            gauge_wrapper2 = size_heading2.find_next('div', class_='gauge__wrapper')
            if gauge_wrapper2:
                # Find all gauge segments with the 'filled' class
                filled_gauges2 = gauge_wrapper2.find_all('div', class_='gauge__segment--filled')
                total_gauges2 = gauge_wrapper2.find_all('div', class_='gauge__segment')
                size_problem2 = len(filled_gauges2)
                # print(f"Size: {size_problem2} out of {len(total_gauges2)}")

        # Define variables to store section content
        recent_avalanche_activity = ""
        current_snowpack_conditions = ""
        mountain_weather = ""
        sliding_danger = ""

        # Define the headers to search for
        target_headers = [
            "Recent Avalanche Activity",
            "Current Snowpack Conditions",
            "Mountain Weather",
            "Sliding Danger"
        ]

        # Loop through each target header
        for target_header in target_headers:
            # Find the <h2> element with the specific text
            extra_info = soup.find_all(class_='col-12 col-lg-10 col-print-10')
            target_section = None

            # Loop through each section
            for section in extra_info:
                header = section.find('h2', class_='additional-info__header')
                if header and header.get_text(strip=True) == target_header:
                    target_section = section
                    break

            # Check if the target section is found
            if target_section:
                # Find all <p> tags within the target section
                p_tags = target_section.find_all('p')
                if p_tags:
                    # Combine all <p> tag texts into a single string
                    section_text = "\n".join([p_tag.get_text(strip=True) for p_tag in p_tags])
                    # Assign the section content to the respective variable
                    if target_header == "Recent Avalanche Activity":
                        recent_avalanche_activity = section_text
                    elif target_header == "Current Snowpack Conditions":
                        current_snowpack_conditions = section_text
                    elif target_header == "Mountain Weather":
                        mountain_weather = section_text
                    elif target_header == "Sliding Danger":
                        sliding_danger = section_text
            else:
                print(f"{target_header} section not found.")

        # Print or use the content as needed
        # print("Recent Avalanche Activity:")
        # print(recent_avalanche_activity)
        # print("\nCurrent Snowpack Conditions:")
        # print(current_snowpack_conditions)
        # print("\nMountain Weather:")
        # print(mountain_weather)
        # print("\nSliding Danger:")
        # print(sliding_danger)

       

        # Insert data into the database
        data = (title, risk_level_overview, overview, issue_time,valid_time, risk_level_high,risk_d_high, risk_level_alpine,risk_d_alpine,risk_level_sub,risk_d_sub,problem_1,risk_d_problem_1,risk_trend_1,risk_time_of_day,likelihood_problem1,size_problem1,problem_2,risk_d_problem_2,risk_trend_2,risk_time_of_day_2,likelihood_problem2,size_problem2,recent_avalanche_activity,current_snowpack_conditions,mountain_weather,sliding_danger)
        update_database_avalanche(data)

    finally:
        # Close the browser
        driver.quit()
        end = time.time()
        print("Time Taken (s): {:.0f}".format(end-start))

    return()


def time_to_scrape():
    while True:
        time.sleep(20)
        database_avalanche.deleteDB()
        avalanche_advisory_scrape('7')
        time.sleep(3*60*60)
    return()