import WebScraper

# constants
TD_ELEMENT = 'td'
SPAN_ELEMENT = 'span'
STR_DOT = '.'
STR_EMPTY = ''
SITE_PATH = './sites.txt'

# get ranking for specific character from html text
def get_ranking_from_text(text):
    highest_ranking = 0

    # Extract ranking and find highest ranking for given character
    for table in text:
        table_data = []
        for row in table.find_all(TD_ELEMENT):
            row_data = [cell.get_text(strip=True)
                        for cell in row.find_all([SPAN_ELEMENT])]
            if len(row_data) != 0:
                table_data.append(row_data[0])
        for ranking in table_data:
            if (isinstance(ranking, str) and
                ranking.replace(STR_DOT, STR_EMPTY).isnumeric()
                    and round(float(ranking)) > highest_ranking):
                highest_ranking = round(float(ranking))

    return highest_ranking


# main method to create and fill table
def main():
    sites = open(SITE_PATH, "r")
    sites_list = sites.read().split('\n')

    ranking_list = []
    for site in sites_list:
        html_text = WebScraper.get_tables(site)
        ranking_list.append(get_ranking_from_text(html_text))

    for ranking in ranking_list:
        print(ranking)


# run main method
if __name__ == "__main__":
    main()
