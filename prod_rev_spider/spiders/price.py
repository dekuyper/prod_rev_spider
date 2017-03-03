# -*- coding: utf-8 -*-
import datetime
import logging

import scrapy

from ..items import WebPageItem


class PriceSpider(scrapy.Spider):
    crawled = 0
    name = "price"
    allowed_domains = ["www.price.ro"]
    start_urls = (
        'https://www.price.ro/',
    )

    def parse(self, response):
        if response.status != 200:
            logging.warning('Status not ok: %s', response.status)
            return None
        for href in response.xpath('//a/@href'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_page_contents)

    @staticmethod
    def parse_page_contents(self, response):
        self.crawled += 1
        if self.crawled > 200:
            logging.info('Exit the crawler, the 200 urls limit exceeded.')
            return None

        url = response.url
        if response.status != 200:
            logging.warning('Url not found %s. Status is %s', url, response.status)

        logging.info("Visited %s", url)
        title = response.xpath('//title/text()').extract()
        html = response.body
        last_updated = datetime.datetime
        item = WebPageItem(url=url, title=title, html=html, last_updated=last_updated)
        return item
