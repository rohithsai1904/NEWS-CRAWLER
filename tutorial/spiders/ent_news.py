import scrapy
from scrapy.loader import ItemLoader
from tutorial.loader import News



class EntNewsSpider(scrapy.Spider):
    name = 'ent_news' 
	
    start_urls = ['https://timesofindia.indiatimes.com/']
    
    def parse(self, response):    
        ent_page_links = response.css('div.col_l_8.col_m_12.padR32._2aV5P a::attr(href)')
        yield from response.follow_all(ent_page_links, self.parse)
        l= ItemLoader(item=News(), response=response)
        l.add_css('headlines','div.articlepage::attr(data-arttitle)')
        l.add_css('newstext','div.Normal::text')
        l.add_css('imglink','div.coverimg1 img::attr(src)')
        l.add_css('imgcaption','div.coverimg1 img::attr(alt)')
        l.add_value('tag','Entertainment Trending News')
        yield l.load_item() 