# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WebPageItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    buy_button = scrapy.Field()
    last_updated = scrapy.Field()
    head = scrapy.Field()
    body = scrapy.Field()

    def __repr__(self):
        return repr(
            {
                'url': self['url'],
                'title': self['title'],
            }
        )
