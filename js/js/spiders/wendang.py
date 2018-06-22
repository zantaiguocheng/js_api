# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from js.items import JsItem

class WendangSpider(CrawlSpider):
    name = 'wendang'
    allowed_domains = ['www.runoob.com']
    start_urls = ['http://www.runoob.com/js/js-tutorial.html']

    rules = (
        Rule(LinkExtractor(allow=r'js/js-.*?\.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = JsItem()
        item['file_urls'] = [response.url]
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return item
