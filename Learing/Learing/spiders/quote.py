import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider

class QuoteSpider(CrawlSpider):
    name = "quote"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]
    rules = [Rule(LinkExtractor(allow='page/', deny='tag/'), callback='parse' ,follow=True)]

    def parse(self, response):
        for qutes in response.css("div.quote span.text::text").getall():
            yield{
                'quote':qutes
            }
            
