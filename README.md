**Noon Scraper**

A simple web scraper built with Python and Selenium to collect product data from Noon Egypt search results.


** About the Project**

This project allows you to search for any product on Noon Egypt and scrape basic information such as:

Product title

Price after discount

Price before discount

Rating

Product link

The scraped data is saved into a CSV file for further analysis.

This project was created as practice for web scraping using Selenium and BeautifulSoup.


** Technologies Used**

Python

Selenium

BeautifulSoup

WebDriver Manager


** How to Run**

Clone the repository:

git clone https://github.com/your-username/noon-scraper.git
cd noon-scraper

Install the required packages:

pip install -r requirements.txt

Run the script:

python noon_scraper.py

Enter:

The product you want to search for

The number of pages you want to scrape

A CSV file will be generated in the same folder.


** Project Structure**
noon-scraper/
│
├── noon_scraper.py
├── requirements.txt
└── README.md

**Notes**

This scraper depends on Noon’s website structure.

If the website updates its HTML structure, some selectors may need to be updated.

The scraper is intended for educational purposes.

** Future Improvements**

Add headless mode

Improve error handling

Export to Excel format


Add logging
