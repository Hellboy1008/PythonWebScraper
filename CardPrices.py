import WebScraper
import undetected_chromedriver as uc
import time
import random
from tqdm import tqdm
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import atexit

# constants
TR_ELEMENT = 'tr'
SPAN_ELEMENT = 'span'
STR_DOT = '.'
STR_EMPTY = ''
SITE_PATH = './sites.txt'

# patch to suppress WinError 6 on exit
def _patched_del(self):
    try:
        self.quit()
    except Exception:
        pass

uc.Chrome.__del__ = _patched_del

def wait_for_cloudflare(driver, timeout=60):
    """Wait until Cloudflare challenge is passed by checking for actual page content."""
    try:
        WebDriverWait(driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
            and "Just a moment" not in d.title
            and "cf-challenge" not in d.page_source
        )
        time.sleep(2)  # extra buffer after challenge clears
    except Exception:
        pass

def get_driver():
    options = uc.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = uc.Chrome(options=options, version_main=145)
    driver.implicitly_wait(10)  # wait up to 10 seconds for elements to load
    return driver

def get_price_from_text(text):
    price = 0
    for table in text:
        for row in table.find_all(TR_ELEMENT):
            cells = row.find_all('td')
            # look for a row where first cell is 状態A
            if len(cells) >= 2 and cells[0].get_text(strip=True) == '状態A':
                price_text = (cells[1].get_text(strip=True)
                              .replace('円', '')
                              .replace('\xa0', '')  # &nbsp; in Python
                              .replace(',', '')
                              .strip())
                if price_text.isnumeric():
                    price = price_text
    return price

def main():
    with open(SITE_PATH, "r") as f:
        sites_list = [s for s in f.read().splitlines() if s.strip()]

    total = len(sites_list)
    update_interval = max(1, total // 20)
    pricing_list = []

    driver = get_driver()

    # Load first site and wait for user to solve Cloudflare manually
    print("Solving Cloudflare on first load — please complete the challenge in the browser window if prompted...")
    driver.get(sites_list[0])
    wait_for_cloudflare(driver)
    input("Press Enter once the page has fully loaded to begin scraping...")

    try:
        with tqdm(total=total, desc="Scraping sites", unit="site") as pbar:
            for i, site in enumerate(sites_list):
                try:
                    html_text = WebScraper.get_tables_dorasuta(driver, site)
                    wait_for_cloudflare(driver)  # wait after each page load
                    time.sleep(random.uniform(3.0, 6.0))
                    pricing_list.append(get_price_from_text(html_text))
                except Exception as e:
                    tqdm.write(f"Failed to scrape {site}: {e}")
                    pricing_list.append(0)

                if (i + 1) % update_interval == 0 or (i + 1) == total:
                    pbar.update(update_interval if (i + 1) % update_interval == 0 else (i + 1) % update_interval)

    finally:
        driver.quit()

    print("\nResults:")
    for price in pricing_list:
        print(price)

if __name__ == "__main__":
    main()