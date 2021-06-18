import scrapy

from itemloaders.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags


class News(scrapy.Item):
    headlines = scrapy.Field()
    newstext = scrapy.Field(input_processor=MapCompose(remove_tags,lambda x: ' '.join(x.split()),
            lambda x: x.upper()),
        output_processor=Join())
    imglink = scrapy.Field()
    imgcaption = scrapy.Field()
    tag=scrapy.Field()
    
    
   