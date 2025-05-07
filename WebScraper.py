import requests
from bs4 import BeautifulSoup

# constants
HTML_PARSER = 'html.parser'
DOKKAN_TABLE_CLASS = 'pct_40_auto'
DORASUTA_TABLE_CLASS = 'stock'
TABLE_ELEMENT = 'table'
WEB_LOAD_TIME = 10


def get_soup(site):
    page = requests.get(site)
    soup = BeautifulSoup(page.text, HTML_PARSER)
    return soup


def get_tables_dokkan(site):
    soup = get_soup(site)
    return soup.find_all(TABLE_ELEMENT, class_=DOKKAN_TABLE_CLASS)


def get_tables_dorasuta(driver, site):
    driver.get(site)
    driver.implicitly_wait(WEB_LOAD_TIME)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, HTML_PARSER)
    return soup.find_all(TABLE_ELEMENT, class_=DORASUTA_TABLE_CLASS)