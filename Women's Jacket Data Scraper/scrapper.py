import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Initializing WebDriver
def initialize_driver():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")   # for not opening chrome in GUI
    driver = webdriver.Chrome(options=chrome_options)
    return driver


def extract_data(url, category, max_loads=20):  # specify the maximum clicks you want to click on load more button
    driver.get(url)
    time.sleep(2)  # Giving time to load the page

    data = []
    load_count = 0

    while load_count < max_loads:
        product_elements = driver.find_elements(By.CSS_SELECTOR, '.product-tile')  # targeting product elements

        print(f"Found {len(product_elements)} product elements for category: {category}")

        for product in product_elements:
            # Extracting the product details
            brand = "Patagonia"  # Modify in the future if we are extracting from other brands

            # Extracting the product title
            title = product.find_element(By.CSS_SELECTOR, '.product-tile__name').text  # change for other brand(change title selector)

            # Extracting the product URL
            product_url = product.find_element(By.CSS_SELECTOR, 'a.link').get_attribute('href')  # change for other brand(change product URL selector)

            # Extracting the product Image URL
            image_url = product.find_element(By.CSS_SELECTOR,
                                             'a[href^="/product/"][itemprop="url"] meta[itemprop="image"]').get_attribute(
                'content')  # change for other brand(change image url selector)

            # Extracting price information of product
            price_span = product.find_element(By.CSS_SELECTOR, '.color-price.active .value')  # change for other brand(change Price selector)
            price = price_span.get_attribute('content') if price_span else None

            # Extracting rating information of product
            try:
                rating_wrapper = product.find_element(By.CSS_SELECTOR, '.product-tile__rating__stars-wrapper')   # change for other brand(change rating selector)
                rating = rating_wrapper.find_element(By.CSS_SELECTOR, '.sr-only').text.split()[
                    1]
            except:
                rating = None

            # Extracting the review count
            try:
                review_count_text = product.find_element(By.CSS_SELECTOR, '.product-tile__rating').text   # change for other brand(change rating selector)
                review_count = int(review_count_text.split('(')[1].split()[0]) if review_count_text else None
            except:
                review_count = None

            # Filtering out the non-women's jackets
            if "jacket" in title.lower() and "W's" in title:
                data.append([brand, title, product_url, image_url, price, rating, review_count])

        # code for checking if there is load more button or pagination
        # Checking for the presence of the "Load More" button
        load_more_button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-lg.btn-dark')   # change the button  selector for the other brand
        if "disabled" in load_more_button.get_attribute("class"):
            # If the button is disabled then break out of the loop
            break
        else:
            # Javascript code
            # Scroll to the "Load More" button using JavaScript
            driver.execute_script("arguments[0].scrollIntoView();", load_more_button)
            time.sleep(1)

            # Clicking the "Load More" button using JavaScript
            driver.execute_script("arguments[0].click();", load_more_button)

            time.sleep(2)  # Giving time for new products to load
            load_count += 1

    return data

def scrape_and_save_data(brand_url):
    all_data = []

    brand, url = brand_url

    print(f"Scraping data from {brand} for Women's Jacket")
    brand_data = extract_data(url, "Women")
    all_data.extend(brand_data)

    # Save the data to a CSV file
    headers = ["Brand", "Product Title", "Product URL", "Product Image URL", "Product Price", "Rating", "Review Count"]

    with open(f"{brand.lower()}_women_jackets_data.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(all_data)

    print(f"Data extraction and CSV creation is completed for {brand}.")

    # Closing the WebDriver
    driver.quit()

if __name__ == "__main__":
    # Define the brand and its URL and change it for the other brand
    brand_url = ("Patagonia", "https://www.patagonia.com/shop/womens")

    # Initializing the webdriver
    driver = initialize_driver()

    # calling the scrape and save  function
    scrape_and_save_data(brand_url)
