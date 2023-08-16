import WebScraper
import pandas as pd

# constants
BACKSLASH_STR = '/'
POINT_STR = '点'
NAMING_LIST = ['blue', 'green', 'purple', 'orange', 'red']
TD_ELEMENT = 'td'
TH_ELEMENT = 'th'
TR_ELEMENT = 'tr'
TYPE_BLUE_SITE = 'https://kamigame.jp/%E3%83%89%E3%83%83%E3%82%AB%E3%83%' + \
    'B3%E3%83%90%E3%83%88%E3%83%AB/%E3%82%AD%E3%83%A3%E3%83%A9%E3%82%AF%' + \
    'E3%82%BF%E3%83%BC/index-%E9%80%9F%E5%B1%9E%E6%80%A7.html'
TYPE_GREEN_SITE = 'https://kamigame.jp/%E3%83%89%E3%83%83%E3%82%AB%E3%83' + \
    '%B3%E3%83%90%E3%83%88%E3%83%AB/%E3%82%AD%E3%83%A3%E3%83%A9%E3%82%AF' + \
    '%E3%82%BF%E3%83%BC/index-%E6%8A%80%E5%B1%9E%E6%80%A7.html'
TYPE_ORANGE_SITE = 'https://kamigame.jp/%E3%83%89%E3%83%83%E3%82%AB%E3%8' + \
    '3%B3%E3%83%90%E3%83%88%E3%83%AB/%E3%82%AD%E3%83%A3%E3%83%A9%E3%82%A' + \
    'F%E3%82%BF%E3%83%BC/index-%E5%8A%9B%E5%B1%9E%E6%80%A7.html'
TYPE_PURPLE_SITE = 'https://kamigame.jp/%E3%83%89%E3%83%83%E3%82%AB%E3%8' + \
    '3%B3%E3%83%90%E3%83%88%E3%83%AB/%E3%82%AD%E3%83%A3%E3%83%A9%E3%82%A' + \
    'F%E3%82%BF%E3%83%BC/index-%E7%9F%A5%E5%B1%9E%E6%80%A7.html'
TYPE_RED_SITE = 'https://kamigame.jp/%E3%83%89%E3%83%83%E3%82%AB%E3%83%B' + \
    '3%E3%83%90%E3%83%88%E3%83%AB/%E3%82%AD%E3%83%A3%E3%83%A9%E3%82%AF%E' + \
    '3%82%BF%E3%83%BC/index-%E4%BD%93%E5%B1%9E%E6%80%A7.html'
SITES_LIST = [TYPE_BLUE_SITE, TYPE_GREEN_SITE, TYPE_PURPLE_SITE,
              TYPE_ORANGE_SITE, TYPE_RED_SITE]

# create df table from html text


def create_dataframe_table_from_text(text):
    df_tables = []

    # Extract and data for each table
    for table in text:
        table_data = []
        for row in table.find_all(TR_ELEMENT):
            row_data = [cell.get_text(strip=True)
                        for cell in row.find_all([TH_ELEMENT, TD_ELEMENT])]
            table_data.append(row_data)
        df = pd.DataFrame(table_data[1:], columns=table_data[0])
        df_tables.append(df)

    # return concatenated table
    final_df = pd.concat(df_tables, ignore_index=True)
    final_df = final_df.drop(df.columns[0], axis=1)
    final_df.iloc[:, 1] = final_df.iloc[:, 1].str.split(BACKSLASH_STR).str[0]
    final_df.iloc[:, 1] = final_df.iloc[:, 1].str.replace(POINT_STR, '')
    final_df = final_df.drop_duplicates()
    return final_df


# main method to create and fill table
def main():
    for index, site in enumerate(SITES_LIST):
        html_text = WebScraper.get_tables(site)
        df = create_dataframe_table_from_text(html_text)
        df.to_excel(NAMING_LIST[index] + '.xlsx', index=False)


# run main method
if __name__ == "__main__":
    main()
