import requests
from bs4 import BeautifulSoup

HTML_PARSER = 'html.parser'

def get_soup(site):
    page = requests.get(site)
    soup = BeautifulSoup(page.text, HTML_PARSER)
    return soup

def get_tables(site):
    soup = get_soup(site)
    return soup.find('table')