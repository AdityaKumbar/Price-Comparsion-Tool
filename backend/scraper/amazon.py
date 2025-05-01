from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def fetch_amazon_price(product_name: str):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    
    driver = webdriver.Chrome(options=chrome_options)

    try:
        search_url = f"https://www.amazon.in/s?k={product_name.replace(' ', '+')}"
        driver.get(search_url)
        time.sleep(3)

        # Locate product containers
        products = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')
        if not products:
            return {"error": "No products found"}

        # Extract name and price from the first product
        first_product = products[0]
        name = first_product.find_element(By.XPATH, './/span[@class="a-size-medium a-color-base a-text-normal"]').text
        price = first_product.find_element(By.XPATH, './/span[@class="a-price-whole"]').text

        return {
            "platform": "Amazon",
            "product_name": name,
            "price": price
        }
    except Exception as e:
        print("Error:", e)
        return {"error": "Product not found on Amazon"}
    finally:
        driver.quit()
