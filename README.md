# Scrapy Learning Project

This repository contains a basic Scrapy project for educational purposes. It includes a spider (e.g., `Hockey`) that demonstrates web scraping from a practice site like [scrapethissite.com](https://www.scrapethissite.com).

> **Note:** Always scrape websites ethically. Respect `robots.txt` and Terms of Service (TOS). Use practice sites for learning.

---

## Installation

### 1. Install Scrapy

Install Scrapy:

```bash
pip install scrapy


## Verify Installation

```bash
scrapy version


## Create a Scrapy Project

```bash
scrapy startproject myproject
cd myproject


## Create a Spider

Generate a spider using the following command:

```bash
scrapy genspider myspider example.com



## Example: Hockey Spider

```python
import scrapy

class HockeySpider(scrapy.Spider):
    name = 'Hockey'
    start_urls = ['https://www.scrapethissite.com/pages/forms/']

    def parse(self, response):
        for team in response.css('tr.team'):
            yield {
                'name': team.css('td.name::text').get().strip(),
                'year': team.css('td.year::text').get().strip(),
                'wins': team.css('td.wins::text').get().strip(),
                'losses': team.css('td.losses::text').get().strip(),
            }

        next_page = response.css('a.next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)


## Running the Spider

Run the spider and export data to JSON:

```bash
scrapy crawl myspider -O output.json
