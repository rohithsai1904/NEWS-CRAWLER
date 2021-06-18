import scrapy
from scrapy.loader import ItemLoader
from tutorial.loader import News




class NewsSpider(scrapy.Spider):
    name = 'news'

    start_urls = ['https://timesofindia.indiatimes.com/']

    def parse(self, response):
        page_links = response.css('div._3SRP3 a::attr(href)')
        page_links+= response.css('div._1CfcV a::attr(href)  ')
        yield from response.follow_all(page_links, self.parse)
        l= ItemLoader(item=News(), response=response)
        l.add_css('headlines','h1._1Y-96 span::text')
        l.add_css('newstext','div._3YYSt.clearfix::text')
        l.add_css('imglink','div._3gupn img::attr(src)')
        l.add_css('imgcaption','div._3gupn img::attr(alt)')
        l.add_value('tag','Trending News')
        yield l.load_item()  

