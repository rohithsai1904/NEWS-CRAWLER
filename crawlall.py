import scrapy
from twisted.internet import reactor
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess


    
def start_sequentially(process: CrawlerProcess, crawlers: list):
    deferred = process.crawl(crawlers[0])
    if len(crawlers) > 1:
        deferred.addCallback(lambda _: start_sequentially(process, crawlers[1:]))
        

class CrawlAll:
    name="crawlall"
    crawlers = []
    file = open('items.jl', 'w')
    file.close()
    process = CrawlerProcess(settings=get_project_settings())
    for spider_name in process.spiders.list():
        crawlers.append(spider_name)

    start_sequentially(process, crawlers)
    process.start()