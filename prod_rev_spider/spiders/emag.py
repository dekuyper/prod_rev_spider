from datetime import datetime

import scrapy

from ..items import WebPageItem


def get_clean_string(one_element: list):
    """
        Expects a single element list
        Returns the stripped element in the list
    """

    if one_element:
        one_element = one_element.pop()
        one_element = one_element.strip()
    else:
        one_element = None
    return one_element


class EmagSpider(scrapy.Spider):
    name = "emag"
    allowed_domains = ["www.emag.ro"]
    start_urls = []
    buy_tutton_path = '//*[@id="page-skin"]/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div[3]/button'

    def request(self, url, callback):
        """
         wrapper for scrapy.request
        """
        request = scrapy.Request(url=url, callback=callback)
        # request.cookies['cel_id'] = 'lpmagqv0j5108h2skpg73jpgb5'
        request.headers['User-Agent'] = (
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, '
            'like Gecko) Chrome/45.0.2454.85 Safari/537.36')
        return request

    def parse(self, response):
        meta = {'dont_redirect': True, 'handle_httpstatus_list': [302]}
        for href in response.xpath('//a/@href'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_page_contents, meta=meta)

    def parse_page_contents(self, response):
        url = response.url
        title = get_clean_string(response.css('title::text').extract())
        buy_button = get_clean_string(response.xpath(self.buy_tutton_path).extract())
        head = get_clean_string(response.xpath('/html/head').extract())
        body = get_clean_string(response.xpath('/html/body').extract())
        last_updated = datetime.utcnow()

        item = WebPageItem(url=url, title=title, buy_button=buy_button, last_updated=last_updated, head=head, body=body)

        return item
