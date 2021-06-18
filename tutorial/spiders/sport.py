import scrapy
from scrapy.loader import ItemLoader
from tutorial.loader import News



class SportNewsSpider(scrapy.Spider):
    name = 'sport_news' 
	
    start_urls = ['https://timesofindia.indiatimes.com/']
    
    def parse(self, response):    
        sport_page_links = response.css('div._2ofaX._1cORx div.col_l_8.col_m_12.padR32._19nxj a::attr(href)')
        yield from response.follow_all(sport_page_links, self.parse)
        l= ItemLoader(item=News(), response=response)
        l.add_css('headlines','h1._1Y-96 span::text')
        l.add_css('newstext','div._3YYSt.clearfix::text')
        l.add_css('imglink','div._3gupn img::attr(src)')
        l.add_css('imgcaption','div._3gupn img::attr(alt)')
        l.add_value('tag','Sport News')
        yield l.load_item() 