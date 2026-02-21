from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import csv


def scrape_noon(search_query, pages):
    products = []

    # تشغيل المتصفح
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    wait = WebDriverWait(browser, 10)

    try:
        for page in range(1, pages + 1):
            url = f"https://www.noon.com/egypt-en/search/?page={page}&q={search_query}"
            browser.get(url)

            # نستنى المنتجات تظهر
            wait.until(
                EC.presence_of_all_elements_located(
                    (By.CLASS_NAME, "PBoxLinkHandler-module-scss-module__WvRpgq__linkWrapper")
                )
            )

            product_elements = browser.find_elements(
                By.CLASS_NAME,
                "PBoxLinkHandler-module-scss-module__WvRpgq__linkWrapper"
            )

            for product in product_elements:
                soup = BeautifulSoup(product.get_attribute("outerHTML"), "html.parser")

                def get_text(tag, class_name):
                    element = soup.find(tag, {"class": class_name})
                    return element.text.strip() if element else "Not Available"

                title = get_text("h2", "ProductDetailsSection-module-scss-module__Y6u1Qq__title")
                price_after = get_text("strong", "Price-module-scss-module__q-4KEG__amount")
                price_before = get_text("span", "Price-module-scss-module__q-4KEG__oldPrice")
                rate = get_text("div", "RatingPreviewStar-module-scss-module__zCpaOG__textCtr")

                link_tag = soup.find("a")
                link = "https://www.noon.com" + link_tag.get("href") if link_tag else "Not Available"

                products.append({
                    "Title": title,
                    "Price After Discount": price_after,
                    "Price Before Discount": price_before,
                    "Rate": rate,
                    "Link": link
                })

    finally:
        browser.quit()

    return products


def save_to_csv(data, filename):
    if not data:
        print("No data found.")
        return

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    print(f"Data saved successfully to {filename}")


if __name__ == "__main__":
    query = input("What are you looking for? ")
    pages = int(input("How many pages do you want to scrape? "))

    scraped_data = scrape_noon(query, pages)
    save_to_csv(scraped_data, f"{query}.csv")