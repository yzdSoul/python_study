import requests

import logging

import multiprocessing

import re

import pymongo

from lxml import etree as et

from urllib.parse import urljoin

logging.basicConfig(level=logging.INFO,

                    format='%(asctime)s - %(levelname)s: %(message)s')

BASE_URL = 'https://static1.scrape.cuiqingcai.com'

TOTAL_PAGE = 10

MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'movies'
MONGO_COLLECTION_NAME = 'movies'
client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
db = client['movies']
collection = db['movies']


def save_data(data):
    collection.update_one({
        'name': data.get('name')
    }, {
        '$set': data
    }, upsert=True)


def scrape_page(url):

    logging.info('scraping %s...', url)

    try:

        response = requests.get(url)

        if response.status_code == 200:

            return response.text

        logging.error('get invalid status code %s while scraping %s', response.status_code, url)

    except requests.RequestException:

        logging.error('error occurred while scraping %s', url, exc_info=True)


def scrape_index(page):

    index_url = f'{BASE_URL}/page/{page}'

    return scrape_page(index_url)


def parse_index(html):

    doc = et.HTML(html)

    result = doc.xpath('//a[@class="name"]')

    for link in result:

        href = link.xpath('@href')[0]

        detail_url = urljoin(BASE_URL, href)

        logging.info('get detail url %s', detail_url)

        yield detail_url


def scrape_detail(url):

    return scrape_page(url)


def parse_detail(html,detail_url):

    doc = et.HTML(html)

    cover = doc.xpath('//img[@class="cover"]/@src')[0]

    name = doc.xpath('//a/h2/text()')[0]

    categories = [item for item in doc.xpath('//div[@class="categories"]/button/span/text()')]

    published_at = doc.xpath('//*[contains(text(),"上映")]/text()')[0]

    published_at = re.search('(\d{4}-\d{2}-\d{2})', published_at).group(1) if published_at and re.search('\d{4}-\d{2}-\d{2}', published_at) else None

    drama = doc.xpath('//div[@class="drama"]/p/text()')[0]

    score = doc.xpath('//p[contains(@class,"score")]/text()')[0]

    score = float(score) if score else None

    logging.error('error get detail url %s', detail_url)

    return {

        'cover': cover,

        'name': name,

        'categories': categories,

        'published_at': published_at,

        'drama': drama,

        'score': score

    }


def main(page):

    index_html = scrape_index(page)

    detail_urls = parse_index(index_html)

    for detail_url in detail_urls:

        detail_html = scrape_detail(detail_url)

        data = parse_detail(detail_html,detail_url)

        logging.info('get detail data %s', data)

        logging.info('saving data to mongodb')

        save_data(data)

        logging.info('data saved successfully')


if __name__ == '__main__':

    pool = multiprocessing.Pool()

    pages = range(1, TOTAL_PAGE + 1)

    pool.map(main, pages)

    pool.close()

    pool.join()
