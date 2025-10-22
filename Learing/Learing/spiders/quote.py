import scrapy


class QuoteSpider(scrapy.Spider):
    name = "quote"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        for qutes in response.css("div.quote"):
            span1, span2 = qutes.css("span")
            
            author_name = span2.css("small::text").get()
            quote = span1.css('::text').get()
            
            tags = qutes.css("div.tags a::text").getall()
            
            yield{
                "author":author_name,
                "quote":quote,
                "tags":tags
            }
