import WebScraper
import math
from tqdm import tqdm

TD_ELEMENT = 'td'
SPAN_ELEMENT = 'span'
STR_DOT = '.'
STR_EMPTY = ''
SITE_PATH = './sites.txt'

def get_ranking_from_text(text):
    rankings = []
    for table in text:
        for row in table.find_all(TD_ELEMENT):
            for cell in row.find_all(SPAN_ELEMENT):
                value = cell.get_text(strip=True)
                if value.replace(STR_DOT, STR_EMPTY).isnumeric():
                    rankings.append(math.ceil(float(value)))
    return max(rankings, default=0)

def main():
    with open(SITE_PATH, "r") as f:
        sites_list = [s for s in f.read().splitlines() if s.strip()]

    total = len(sites_list)
    update_interval = max(1, total // 20)  # every 5% (100% / 20 steps)
    ranking_list = []

    with tqdm(total=total, desc="Scraping sites", unit="site") as pbar:
        for i, site in enumerate(sites_list):
            try:
                html_text = WebScraper.get_tables_dokkan(site)
                ranking_list.append(get_ranking_from_text(html_text))
            except Exception as e:
                tqdm.write(f"Failed to scrape {site}: {e}")
                ranking_list.append(0)

            if (i + 1) % update_interval == 0 or (i + 1) == total:
                pbar.update(update_interval if (i + 1) % update_interval == 0 else (i + 1) % update_interval)

    print("\nResults:")
    for ranking in ranking_list:
        print(ranking)

if __name__ == "__main__":
    main()