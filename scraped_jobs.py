import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Define the URL of the target website to scrape
base_url = "https://realpython.github.io/fake-jobs/"

# Define a user-agent header, to identify who we are
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
}

print("Connecting to the website...")

response_page = requests.get(base_url, headers=header)

if response_page.status_code == 200:
    print("Connected Successfully")
else:
    print("Connection not successful!")

# To parse the HTML content of the page
parsed_page = BeautifulSoup(response_page.text, "html.parser")

# To find all the job listing elements on the page
job_listings = parsed_page.find_all("div", class_="card")

# Initialize an empty list to store the extracted job data
all_jobs_data = []

print("Extracting job data...")
for job in job_listings:
    # Extract the job title
    title_element = job.find("h2", class_="title")
    job_title = title_element.text.strip() if title_element else "N/A"

    # Extract the company name
    company_element = job.find("h3", class_="company")
    company_name = company_element.text.strip() if company_element else "N/A"

    # Extract the location details
    location_element = job.find("p", class_="location")
    location_text = location_element.text.strip() if location_element else "N/A"
    location_parts = location_text.split(", ")
    city = location_parts[0].strip() if len(location_parts) > 0 else "N/A"
    state = location_parts[1].strip() if len(location_parts) > 1 else "N/A"

    # Extract the date posted
    date_element = job.find("p", class_="is-small has-text-grey")
    date_posted_str = date_element.text.strip() if date_element else "N/A"

    # Initialize date-related variables
    day_of_week_day_month = "N/A"
    year = "N/A"
    date_posted_datetime = None

    if date_posted_str != "N/A":
        try:
            date_posted_datetime = datetime.strptime(date_posted_str, "%Y-%m-%d")
            day_of_week_day_month = date_posted_datetime.strftime("%A, %d %B")
            year = date_posted_datetime.year
        except ValueError:
            print(f"Warning: Could not parse date string: {date_posted_str}")
            date_posted_datetime = None  # Set to None to avoid furher issues

       # To store the extracted data in a dictionary
    job_data = {
        "Job Title": job_title,
        "Company Name": company_name,
        "Location (City)": city,
        "Location (State)": state,
        "Date Posted (Original)": date_posted_str,
        "Date Posted (Datetime)": date_posted_datetime,
        "Day of Week, Day and Month": day_of_week_day_month,
        "Year": year,
     }
    all_jobs_data.append(job_data)

# To convert the list of dictionaries to a Pandas DataFrame
df_jobs = pd.DataFrame(all_jobs_data)

# Print the resulting DataFrame, first 20 records
print("\nExtracted Job Data:")
df_jobs.head(20)

# To save the DataFrame to a CSV file as required
df_jobs.to_csv("scraped_jobs.csv", index=False)
print("\nJob data saved to scraped_jobs.csv")

