import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from datablogger_scraper.items import DatabloggerScraperItem
class MySpider(CrawlSpider):
    name = 'MySpider'
    start_urls = ["https://www.data-blogger.com/"]

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=())),

    )

    def parse_item(self, response):
         item =DatabloggerScraperItem()
         item['url_from'] = response.url
         item['url_to'] = response.url
         return item