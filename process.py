import scrape


def process_scraped_data():
    elements = scrape.scrape_new_carhartt_sale_items()
    processed_data_dict = {}
    for element in elements:
        processed_data_dict[element.find_all('img')[2]['alt']] = "https://www.carhartt.com" + element.find_all('a')[0]['href']
    return processed_data_dict