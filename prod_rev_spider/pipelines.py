# -*- coding: utf-8 -*-
from pymongo import MongoClient
from scrapy.exceptions import DropItem


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ProductPagePipeline(object):
    def process_item(self, item, spider):
        if 'buy_button' in item.keys() and item['buy_button'] is not None:
            del item['buy_button']
            return item
        else:
            raise DropItem("Not product page")


class DuplicatesPipeline(object):
    def __init__(self):
        self.urls_seen = set()

    def process_item(self, item, spider):
        if item['url'] in self.urls_seen:
            raise DropItem("Duplicate item found: %s".format(item['title']))
        else:
            self.urls_seen.add(item['url'])
            return item


class DatabaseStorage(object):
    collection_name = 'WebPageItem'

    def __init__(self, mongo_uri, mongo_db):
        self.client = MongoClient(mongo_uri)
        self.db = self.client[mongo_db]

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if self.db[self.collection_name].find_one({'url': item['url']}):
            raise DropItem('Item already in db')
        self.db[self.collection_name].insert(dict(item))

        return item
