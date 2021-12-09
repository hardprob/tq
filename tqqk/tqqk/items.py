# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TqqkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    日期=scrapy.Field()
    最高温=scrapy.Field()
    最低温=scrapy.Field()
    天气=scrapy.Field()
    风力风向=scrapy.Field()
    地区=scrapy.Field()


