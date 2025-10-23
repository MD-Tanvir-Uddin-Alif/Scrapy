import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class HockeySpider(CrawlSpider):
    name = "Hockey"
    allowed_domains = ["www.scrapethissite.com"]
    start_urls = ["https://www.scrapethissite.com/pages/forms/"]
    rules = [Rule(LinkExtractor(allow=r'page_num=\d+'), callback='parse', follow=True)]  #made for pagination

    def parse(self, response):
        team_row = response.css("table.table tr.team") # got all the table
        
        
        for team_info in team_row:    # going through all the table
            
            team_name = team_info.css("td.name::text").get().strip()
            team_year = team_info.css("td.year::text").get().strip()
            team_wins = team_info.css("td.wins::text").get().strip()
            team_losses = team_info.css("td.losses::text").get().strip()
            
            
            # saving the data to a json file
            yield{
                "Team Name": team_name,
                "Team Year": team_year,
                "Team Wins": team_wins,
                "Team Losses": team_losses
            }
