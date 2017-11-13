import scrapy
import csv
from scrapy.linkextractor import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from datablogger_scraper.items import DatabloggerScraperItem
from scrapy.conf import settings

class DatabloggerSpider(scrapy.Spider):

    custom_settings = {'DEPTH_LIMIT': 200,}
    
    
    # The name of the spider
    name = "datablogger"
    allowed_domains = ["data-blogger.com"]
    # The domains that are allowed (links to other domains are skipped)
    linksvisited=[]
    linksvisited.append("https://www.data-blogger.com")
    linksvisited.append("https://www.data-blogger.com/")
    

    # The URLs to start with
    start_urls = ["https://www.data-blogger.com/"]
        # This spider has one rule: extract all (unique and canonicalized) links, follow them and parse them using the parse_items method
    
    # Method for parsing items
    def parse(self, response):
        items=[]
        links = response.css('a::attr(href)').extract()
        DatabloggerSpider.linksvisited.append(response.url)
        linksn=[]
        if links:
           linksn= list(set(links)- set(DatabloggerSpider.linksvisited)) 
        i=0
        for url in linksn:
           
           if url not in DatabloggerSpider.linksvisited  :
              item = []
              item.append(response.url)
              item.append(url)
              item.append(response.css('title::text').extract())
              yield scrapy.Request( url,callback=self.parse)
              with open("/home/kanchana/Big_data_class/big-data-python-class/Homeworks/Homework7/datablogger_scraper/links.csv", 'a') as myfile:
                 wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                 wr.writerow(item) 
                 
