from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
from bs4 import BeautifulSoup

# Set up the WebDriver using ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navigate to the IMDb reviews page
url = "https://www.imdb.com/title/tt1190634/reviews/"
driver.get(url)

# Optional: Wait for some time to ensure the page fully loads
time.sleep(5)

# Function to load all reviews by clicking the "Load More" button
def load_all_reviews():
    while True:
        try:
            # Wait for the "Load More" button to be clickable
            load_more_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "load-more-trigger"))
            )
            load_more_button.click()
            time.sleep(5)  # Increased delay to allow reviews to load
        except:
            # If the "Load More" button is not found or clickable, break the loop
            break

# Load all reviews
load_all_reviews()

# Parse the page source using BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find all review containers
review_containers = soup.find_all('div', class_='lister-item mode-detail imdb-user-review collapsable')

# Debugging: Print the number of review containers found
print(f"Number of reviews found: {len(review_containers)}")

# Open a CSV file to write the data
with open(r'C:\Users\ankit\Downloads\data\imdb_reviews.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Rating', 'Review Title']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for container in review_containers:  # Iterate through all review containers
        # Extract rating details
        rating_container = container.find('span', class_='rating-other-user-rating')
        if rating_container:
            rating = rating_container.find('span').get_text(strip=True)  # Extract the rating score
        else:
            rating = 'N/A'
        
        # Extract review details
        review_title = container.find('a', class_='title').get_text(strip=True) if container.find('a', class_='title') else 'N/A'
        
        # Write the review data to the CSV file immediately
        writer.writerow({'Rating': rating, 'Review Title': review_title})

# Close the WebDriver
driver.quit()