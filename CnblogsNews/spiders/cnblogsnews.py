# -*- coding: utf-8 -*-
from urllib import parse

import scrapy
from scrapy import Request

class CnblogsnewsSpider(scrapy.Spider):
    name = 'cnblogsnews'
    allowed_domains = ['news.cnblogs.com']
    start_urls = ['http://news.cnblogs.com/']

    def parse(self, response):
        post_nodes = response.css("#news_list .content")
        for post_node in post_nodes:
            img_url = post_node.css(".entry_summary img::attr(src)").extract_first("")
            post_url = post_node.css("h2 a::attr(href)").extract()
            yield Request(url=parse.urljoin(response.url, post_url),meta={'front_image':img_url},callback=self.parse_detail)

        # 获取下一页链接
        next_url = response.css('.pager a::attr(href)').extract()[-1]
        if next_url:
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)


    def parse_detail(self,response):
        pass