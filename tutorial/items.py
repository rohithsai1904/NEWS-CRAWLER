# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class News(scrapy.Item):
    headlines = scrapy.Field()
    newstext = scrapy.Field()
    imglink = scrapy.Field()
    imgcaption = scrapy.Field()
    