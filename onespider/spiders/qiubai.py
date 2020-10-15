# -*- coding: utf-8 -*-
import scrapy
from onespider.items import OnespiderItem


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['http://www.qiushibaike.com/text/']

    def parse(self, response):

        text_list = response.xpath("/html/body/div[@id='content']/div[@class='content-block clearfix']/div[@class='col1 old-style-col1']/div")
        
        texts = []

        # print(text_list)
        
        for text in text_list:

            item = OnespiderItem()

            item['name'] = text.xpath("./div/a[2]/h2/text()").extract()[0]
            # print(item)
            item['text'] = text.xpath("./a/div/span").extract()[0]
            # print(item)
            texts.append(item)
        
        
        
        return texts
