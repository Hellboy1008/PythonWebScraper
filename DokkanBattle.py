import WebScraper

type_blue = 'https://kamigame.jp/%E3%83%89%E3%83%83%E3%82%AB%E3%83%B3%E3%83%90%E3%83%88%E3%83%AB/%E3%82%AD%E3%83%A3%E3%83%A9%E3%82%AF%E3%82%BF%E3%83%BC/index-%E9%80%9F%E5%B1%9E%E6%80%A7.html'
type_green = 'https://kamigame.jp/%E3%83%89%E3%83%83%E3%82%AB%E3%83%B3%E3%83%90%E3%83%88%E3%83%AB/%E3%82%AD%E3%83%A3%E3%83%A9%E3%82%AF%E3%82%BF%E3%83%BC/index-%E6%8A%80%E5%B1%9E%E6%80%A7.html'
type_purple = 'https://kamigame.jp/%E3%83%89%E3%83%83%E3%82%AB%E3%83%B3%E3%83%90%E3%83%88%E3%83%AB/%E3%82%AD%E3%83%A3%E3%83%A9%E3%82%AF%E3%82%BF%E3%83%BC/index-%E7%9F%A5%E5%B1%9E%E6%80%A7.html'
type_orange = 'https://kamigame.jp/%E3%83%89%E3%83%83%E3%82%AB%E3%83%B3%E3%83%90%E3%83%88%E3%83%AB/%E3%82%AD%E3%83%A3%E3%83%A9%E3%82%AF%E3%82%BF%E3%83%BC/index-%E5%8A%9B%E5%B1%9E%E6%80%A7.html'
type_red = 'https://kamigame.jp/%E3%83%89%E3%83%83%E3%82%AB%E3%83%B3%E3%83%90%E3%83%88%E3%83%AB/%E3%82%AD%E3%83%A3%E3%83%A9%E3%82%AF%E3%82%BF%E3%83%BC/index-%E4%BD%93%E5%B1%9E%E6%80%A7.html'
html_text = WebScraper.get_tables(type_blue)

print(html_text)