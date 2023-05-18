from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

url = 'https://coinmarketcap.com/currencies/bitcoin/'
driver = webdriver.Chrome('chromedriver')
driver.get(url)

# Wait for the "load more" button to become clickable
load_more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-qa-id="load-more-button"]')))

while load_more_button:
    # Click the "load more" button
    load_more_button.click()

    # Wait for the new content to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//tbody')))

    # Get the new HTML content and parse it with Beautiful Soup
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Extract the Bitcoin data from the table
    table_rows = soup.find_all('tr')
    for row in table_rows:
        cells = row.find_all('td')
        if cells:
            name = cells[2].text.strip()
            if name == 'Bitcoin':
                price = cells[3].text.strip()
                market_cap = cells[6].text.strip()
                volume = cells[7].text.strip()
                print(f'Price: {price} Market Cap: {market_cap} Volume: {volume}')

    # Check if there are more "load more" buttons to click
    load_more_button = driver.find_element_by_xpath('//button[@data-qa-id="load-more-button"]') if driver.find_elements_by_xpath('//button[@data-qa-id="load-more-button"]') else None

# Close the browser
driver.quit()