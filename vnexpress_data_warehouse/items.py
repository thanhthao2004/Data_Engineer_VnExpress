# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VnexpressDataWarehouseItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    location = scrapy.Field()
    disease_name = scrapy.Field()
    count_comments = scrapy.Field()
    total_like = scrapy.Field()
    content = scrapy.Field()
    