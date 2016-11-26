# -*- coding: utf-8 -*-

# import scrapy  # 可以写这句注释下面两句，不过下面要更好
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from dmoz.items import DmozItem  # 此处如果报错是pyCharm的原因

class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["heartsong.top"]  # 允许爬取的域名，非此域名的网页不会爬取
    start_urls = [
        "http://www.heartsong.top/forum.php?mod=viewthread&tid=8"  # 起始url，此例只爬这个页面
    ]

    def parse(self, response):
        selector = HtmlXPathSelector(response)  # 创建选择器

        table = selector.select('//*[starts-with(@id, "pid")]')  # 取出所有的楼层
        for each in table:  # 对于每一个楼层执行下列操作
            item = DmozItem()  # 实例化一个Item对象
            item['title'] = selector.select('//*[@id="thread_subject"]/text()').extract()[0]
            item['author'] = \
                each.select('tr[1]/td[@class="pls"]/div[@class="pls favatar"]/div[@class="pi"]/div[@class="authi"]/a/text()').extract()[0]
            item['post_time'] = \
                each.select('tr[1]/td[@class="plc"]/div[@class="pi"]').re(r'[0-9]+-[0-9]+-[0-9]+ [0-9]+:[0-9]+:[0-9]+')[0].decode("unicode_escape")
            content_list = each.select('.//td[@class="t_f"]').select('string(.)').extract()
            content = "".join(content_list)  # 将list转化为string
            item['url'] = response.url  # 用这种方式获取网页的url
            # 把内容中的换行符，空格等去掉
            item['content'] = content.replace('\r\n', '').replace(' ', '').replace('\n', '')
            print "I am a test  point"

def _init_main(item):

            file = open("items.txt", "a")  # 以追加的方式打开文件，不存在则创建
            # 因为item中的数据是unicode编码的，为了在控制台中查看数据的有效性和保存，
             # 将其编码改为utf-8
            item_string = str(item).decode("unicode_escape").encode('utf-8')
            file.write(item_string)
            file.write('\n')
            file.close()
            print item_string  # 在控制台输出
            #return item  # 会在控制台输出原item数据，可以选择不写
            yield item  # 将创建并赋值好的Item对象传递到PipeLine当中进行处理