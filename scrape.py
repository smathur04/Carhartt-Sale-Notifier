from bs4 import BeautifulSoup
import requests


def scrape_new_carhartt_sale_items():
    url = "https://www.carhartt.com/c/sale-mens-tops"
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    tag_name = 'car-product-grid-item'
    elements = soup.find_all(tag_name)
    return elements
