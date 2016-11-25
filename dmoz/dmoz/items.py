# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field


class DmozItem(Item):
    # define the fields for your item here like:
    # name = Field()
    title = Field()
    url = Field()
    author = Field()
    post_time=Field()
    content=Field()
