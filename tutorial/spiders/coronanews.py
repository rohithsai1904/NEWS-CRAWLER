import scrapy
from scrapy.loader import ItemLoader
from tutorial.loader import News



class CorNewsSpider(scrapy.Spider):
    name = 'cor_news' 
	
    start_urls = ['https://timesofindia.indiatimes.com/']
    
    def parse(self, response):    
        cor_page_links = response.css('div._2ofaX~div._2ofaX div.col_l_8.col_m_12.padR32._19nxj a::attr(href)')[:9]
        yield from response.follow_all(cor_page_links, self.parse)
        l= ItemLoader(item=News(), response=response)
        l.add_css('headlines','h1._1Y-96 span::text')
        l.add_css('newstext','div._3YYSt.clearfix::text')
        l.add_css('imglink','div._3gupn img::attr(src)')
        l.add_css('imgcaption','div._3gupn img::attr(alt)')
        l.add_value('tag','Corona News')
        yield l.load_item() 