# Assignment_Web_Scraping_Data_Extraction

Project Description

This project was design create a Python script that scrapes or extracts job listing data from the webpage below:

https://realpython.github.io/fake-jobs/

Project Aim
The aim of the project is to use Python for web scraping and using libraries such as requests, BeautifulSoup, Pandas and datetime.

Here's a breakdown of what the script does:
1/ Make request the Web Page: It sends an HTTP request to the URL to get the HTML content of the page.
2/ Parses the HTML: It uses the BeautifulSoup library to parse the HTML, making it easy for Python to navigate and extract specific elements.
3/ Locates Job Listings: It identifies the HTML elements on the page that contain the job listing information by using the relevant tags ('div', 'h2', 'h3', 'p' and various classes).
4/ Extracts Job Data: For each job listing, it extracts the following information:
(i) Job Title
(ii) Company Name
(iii) Location (City and State)
(iv) Date Posted:
(a) The date posted was converted to datetime object.
(b) The Date posted was further parsed to create two additional columns. One containing the day of week, day and month, and the second column containing the year.

5/ Stores the data in a DataFrame: It organizes the extracted data into a Pandas DataFrame, a tabular data structure that is convenient for data analysis and for data scientists
6/ Prints the DataFrame: Finally, it prints the DataFrame, displaying the extracted job data in a structured format. The first 20 data were display using df_jobs.head(20)
7/ Saves to CSV: The script also saves the DataFrame to a CSV file (scraped_jobs.csv).

How to Run the Script
Follow these steps to run the script:
Prerequisites:
Python: This must be installed and install the following Python libraries: 
pandas
requests
beautifulsoup4

Open a terminal or command prompt and run the following command:
pip install pandas requests beautifulsoup4

create a virtual environment and activate it

Create and save the Script: Save the Python code into a named file e.g. scraped_jobs.py.

Run the Script: Execute the script by running the following command:
python scraped_jobs.py or clicking the Run button

The script will connect to the website, extract the job data, display the data in a dataframe in the console, and save it to a CSV file.
