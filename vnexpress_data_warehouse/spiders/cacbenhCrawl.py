# main.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from random import randint
from bs4 import BeautifulSoup
import pandas as pd
import ssl, os
ssl._create_default_https_context = ssl._create_stdlib_context
os.makedirs('screenshots', exist_ok=True)

home_url = 'https://pharmed.vn/exhibitors'
url_companies = home_url + '/companies?page={page_number}'
url_detail = home_url + '/company/{company_id}'

# Khởi tạo ChromeDriver
service = Service(ChromeDriverManager().install())

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("disable-notifications")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--incognito')

def csv_to_xlsx(path):
    """
    Converts a CSV file to an XLSX file.
    
    Args:
    path: Path to the input CSV file.
    """
    # Read the CSV file
    df = pd.read_csv(path)
    
    # Save to an Excel file
    df.to_excel(f'{path[:-4]}.xlsx', index=False)
    return True

def scroll_down_until_element_found(driver, xpath, scroll_pause_time=1):
    """
    Scrolls down the page until the element specified by the given XPath is found.
    
    Args:
    driver: WebDriver object (Selenium).
    xpath: XPath string to locate the target element.
    scroll_pause_time: Time in seconds to pause between scrolls (default: 1).
    """
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        try:
            # Check if the element is present on the page
            element = driver.find_element(By.XPATH, xpath)
            if element:
                print("Element found!")
                break
        except NoSuchElementException:
            pass

        # Scroll down to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Wait for the page to load
        sleep(scroll_pause_time)

        # Calculate new scroll height and compare with the last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            print("Reached the bottom of the page, element not found.")
            break

        last_height = new_height

def enter_code(driver):
    '''
    Accept the code and submit the search form

    Args:
    driver: WebDriver object (Selenium).
    '''
    input_xpath = '//div[@class="job-field"]//input'
    keyword = 'JP3HP'
    driver.find_element(By.XPATH, input_xpath).send_keys(keyword)
    print(f'Entered keyword: {keyword}')
    sleep(1)
    submit_xpath = '//button[@type="submit"]'
    driver.find_element(By.XPATH, submit_xpath).click()
    print('Submitted search form')
    sleep(1)

def get_company_info(driver):
    '''
    Get company information
    
    Args:
    driver: WebDriver object (Selenium).
    '''
    data = {}
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    data['name'] = soup.find('div', class_='job-single-info3').h3.text
    data['logo'] = soup.find('div', class_='job-thumb').img['src']
    data['address'] = soup.find('div', class_='job-single-info3').span.text.split('Địa chỉ:')[-1].strip()
    data['description'] = soup.find('div', class_='job-single-info3').find('ul').find_all('li')[0].text.strip()
    data['about'] = soup.find('div', class_='job-details').p.text
    overviews = soup.find('div', class_='job-overview').find('ul').find_all('li')
    overviews = {item.find('h3').text.lower(): item.find('span').text.strip() for item in overviews}
    data.update(overviews)
    return data

def get_link(driver, pages):
    '''
    Get company links
    
    Args:
    driver: WebDriver object (Selenium).
    pages: List of page numbers.
    '''
    links = []
    for page_number in pages:
        driver.get(url_companies.format(page_number=page_number))
        sleep(randint(1, 2))
        page_xpath = '//div[@class="pagination pagination-homepage-v2"]'
        scroll_down_until_element_found(driver, page_xpath)
        link_path = '//div[@class="job-title-sec"]//h3//a'
        link = driver.find_elements(By.XPATH, link_path)
        links.extend([l.get_attribute('href') for l in link])
    return links

def get_data(driver, links, output = 'pharmed.csv'):
    '''
    Get company data

    Args:
    driver: WebDriver object (Selenium).
    links: List of company links.
    output: Output file path.
    '''
    stop_xpath = '//footer[@class="style2"]'
    for idx, link in enumerate(links, 1):
        try:
            print(f'> {idx}/{len(links)} -> {link}')
            driver.get(link)
            sleep(randint(1, 2))
            scroll_down_until_element_found(driver, stop_xpath)
            data = get_company_info(driver)
            name_screen = link.split('/')[-1]
            driver.save_screenshot(f"./screenshots/{name_screen}.png")
            data['link'] = link
            df = pd.DataFrame([data])
            df.to_csv(output, index=False, mode='a', header=not os.path.exists(output))
        except Exception as e:
            write_log(f'> {idx}/{len(links)} -> {link}: {e}')

def write_log(text):
    '''
    Write log to file

    Args:
    text: Log message.
    '''
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(text+'\n')

if __name__ == "__main__":
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url_companies.format(page_number=1))
    sleep(randint(1, 2))
    enter_code(driver)
    links = get_link(driver, range(1, 25))
    get_data(driver, links)
    driver.quit()