import requests
from bs4 import BeautifulSoup

# constants
HTML_PARSER = 'html.parser'
TABLE_CLASS = 'pct_20_60_aunto'
TABLE_ELEMENT = 'table'


def get_soup(site):
    page = requests.get(site)
    soup = BeautifulSoup(page.text, HTML_PARSER)
    return soup


def get_tables(site):
    soup = get_soup(site)
    return soup.find_all(TABLE_ELEMENT, class_=TABLE_CLASS)
