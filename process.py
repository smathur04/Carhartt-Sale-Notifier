import scrape


def process_scraped_data():
    elements = scrape.scrape_new_carhartt_sale_items()
    for element in elements:
        print([element.find_all('img')[2]['alt'], "https://www.carhartt.com" + element.find_all('a')[0]['href']])