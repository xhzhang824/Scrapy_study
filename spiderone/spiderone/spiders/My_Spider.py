# -*- coding: utf-8 -*-
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider


class My_Spider(BaseSpider):
    name = "MySpider"
    allowed_domains=["aiting.cf"]
    start_urls = [
        "http://www.aiting.cf"  # 起始url，此例只爬这个页面
    ]
    def parse(self, response):
        selector=HtmlXPathSelector(response)
        text=selector.select('/html/body/article')
        info=text.select('string(.)').extract()
        string = str(info).decode("unicode_escape").encode('utf-8')
        print string
        content=string.replace('\n','').replace(' ','')
        print content
        file = open("items.txt", "w")  # 以追加的方式打开文件，不存在则创建
        file.write(content)
        file.close()
