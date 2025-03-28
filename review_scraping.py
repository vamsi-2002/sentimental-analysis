from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time

# Initialize Selenium WebDriver
driver = webdriver.Chrome()  # Ensure you have the ChromeDriver installed and in PATH
url = "https://www.amazon.in/Apple-New-iPhone-12-128GB/dp/B08L5TNJHG/"
driver.get(url)  # Redirect to Amazon login page
# Wait for the login fields to be visible
wait = WebDriverWait(driver, 20)
sign_in_hover = wait.until(EC.element_to_be_clickable((By.ID, "nav-link-accountList")))
sign_in_hover.click()


# Provide Amazon login credentials
username = " "    # Replace with your email or mobile No
password = " "   # Replace with your password


email_field = wait.until(EC.presence_of_element_located((By.ID, "ap_email")))
email_field.send_keys(username)

# Click continue
driver.find_element(By.ID, "continue").click()

# Enter password
password_field = wait.until(EC.presence_of_element_located((By.ID, "ap_password")))
password_field.send_keys(password)

# Submit login form
driver.find_element(By.ID, "signInSubmit").click()

# Navigate to the product review page
driver.get(url)

# Wait for the page to load
reviews_data = []

driver.get(url)

# Wait for the page to load
wait = WebDriverWait(driver, 20)

# List to store scraped data
reviews_data = []

# Function to extract reviews from a single page
def extract_reviews():
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    reviews = soup.select('div[data-hook="review"]')
    
    for review in reviews:
        try:
            # Extract review title (text next to stars)
            title = review.select_one("a[data-hook='review-title']").text.split("\n")[1]
        except AttributeError:
            title = "not mentioned"

        try:
            # Extract review text (user's review)
            review_text = review.select_one('span[data-hook="review-body"]').text.strip()
        except AttributeError:
            review_text = "not mentioned"

        try:
            # Extract color (if present)
            # color = review.select_one('span.a-size-mini.a-color-secondary').text.strip().split('Colour:')[1].split('Size:')[0].strip()
            # color = review.select_one('span.a-color-secondary').text
            color = review.select_one('div.a-row.a-spacing-mini.review-data.review-format-strip').text.strip().split('Colour:')[1].split('Size:')[0].strip()
            style_name = review.select_one('div.a-row.a-spacing-mini.review-data.review-format-strip').text.strip().split('Size:')[1].split('Pattern Name:')[0].strip()
            
        except (AttributeError, IndexError): 
            color = "not mentioned"
            style_name = "not mentioned"

        # Check if the review is a verified purchase
        verified_purchase = 'Yes' if review.select_one('span[data-hook="avp-badge"]') else 'No'
        
        # Append data to the list
        reviews_data.append([title, review_text,style_name, color, verified_purchase])
status = True
# Paginate through all review pages
while True:
    extract_reviews()
    if status:
        show_more_reviews = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.a-link-emphasis.a-text-bold')))
        show_more_reviews.click()
        time.sleep(5)
        status = False
    try:
        # Click the "Next" button to go to the next page
        next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.a-last a')))
        next_button.click()
        time.sleep(5)  # Allow time for the next page to load
    except Exception as e:
        print("No more pages to scrape.")
        break

# Save scraped data to a CSV file
df = pd.DataFrame(reviews_data, columns=['Review_Title', 'Review_Text', 'Style_Name', 'Colour', 'Verified_Purchase'])
df.to_csv('iphone_reviews.csv', index=False)

print("Scraping completed. Data saved to iphone_reviews.csv")
driver.quit()