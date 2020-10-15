# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import csv



class OnespiderPipeline(object):
    def __init__(self):
        pass

    def open_spider(self,spider):
        print('OOOOOOOOOOOOOO-爬虫开启了OOOOOOOOOOOOOO')
        print(spider)
        self.conn = pymysql.connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'root',
            password = 'qin5812555',
            db = 'scrapy',
            charset = 'utf8'
        )
        self.cur = self.conn.cursor()

        

    
    def process_item(self, item, spider):
        print('----------运行中---------------')
        sql = "INSERT INTO qiubai(id,name,text) VALUES(NULL,'%s','%s')"%(item['name'],item['text'])
        # print(sql)
        self.cur.execute(sql)
        self.conn.commit()
        return item
    
    def close_spider(self,spider):
        print("#############爬虫关闭################")
        self.conn.close()
        self.cur.close()

