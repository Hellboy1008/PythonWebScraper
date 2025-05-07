import WebScraper
import math
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# constants
TR_ELEMENT = 'tr'
SPAN_ELEMENT = 'span'
STR_DOT = '.'
STR_EMPTY = ''
SITE_PATH = './sites.txt'

# web driver options
options = Options()
options.headless = False
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')

# get ranking for specific character from html text
def get_price_from_text(text):
    price = 0

    # Extract ranking and find highest ranking for given character
    for table in text:
        table_data = []
        for row in table.find_all(TR_ELEMENT):
            condition = row.find('td', class_='condition')
            if condition and condition.text == '状態A':
                price_html = row.find('td', class_='price')
                if price_html:
                    price_text = price_html.text.strip().replace('円', '').replace('&nbsp;', '').replace(',', '')
                    price = price_text

    return price


# main method to create and fill table
def main():
    sites = open(SITE_PATH, "r")
    sites_list = sites.read().split('\n')

    ranking_list = []
    for site in sites_list:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        html_text = WebScraper.get_tables_dorasuta(driver, site)
        ranking_list.append(get_price_from_text(html_text))
        driver.quit()

    for ranking in ranking_list:
        print(ranking)


# run main method
if __name__ == "__main__":
    main()
