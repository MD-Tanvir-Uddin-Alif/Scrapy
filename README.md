# Scrapy Learning Project

This repository contains a basic Scrapy project for educational purposes. It includes a spider (e.g., `Hockey`) that demonstrates web scraping from a practice site like [scrapethissite.com](https://www.scrapethissite.com). The project covers installation, setup, running spiders, configuring user agents (manual & rotating), and proxy usage.

> **Note:** Always scrape websites ethically. Respect `robots.txt` and Terms of Service (TOS). Use practice sites for learning.

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [1. Install Scrapy](#1-install-scrapy)
  - [2. Create a Scrapy Project](#2-create-a-scrapy-project)
  - [3. Create a Spider](#3-create-a-spider)
- [Running the Spider](#running-the-spider)
- [Configuring User Agents](#configuring-user-agents)
  - [Manual User-Agent](#manual-user-agent)
  - [Auto Rotating User-Agent (`scrapy-fake-useragent`)](#auto-rotating-user-agent-scrapy-fake-useragent)
- [Configuring Proxies](#configuring-proxies)
- [Additional Tips](#additional-tips)
- [Useful Commands](#useful-commands)
- [Disclaimer](#disclaimer)

---

## Prerequisites

- Python 3.8+ (recommended: 3.10 or later)  
- A terminal or command prompt  
- Optional: Virtual environment tool like `venv` or `conda` for dependency isolation

---

## Installation

### 1. Install Scrapy

Create and activate a virtual environment (recommended):

```bash
# Using venv (built-in)
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate

# Or using Conda
conda create -n scrapy-env python=3.10
conda activate scrapy-env



Install Scrapy:

pip install scrapy


Verify installation:

scrapy version

2. Create a Scrapy Project
scrapy startproject myproject
cd myproject


This creates folders like spiders/, settings.py, etc. Replace myproject with your desired project name.

3. Create a Spider

Generate a spider:

scrapy genspider myspider example.com


Edit spiders/myspider.py to define start_urls and parsing logic.

Example: Hockey Spider

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

Running the Spider
scrapy crawl myspider -O output.json


crawl myspider: Runs the spider named "myspider".

-O output.json: Overwrites and exports items to JSON.

Optional verbose logs:

scrapy crawl myspider -O output.json -L DEBUG


Check output.json for scraped data.

Configuring User Agents
Manual User-Agent

In settings.py:

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'


Per spider:

class MySpider(scrapy.Spider):
    custom_settings = {
        'USER_AGENT': 'My Custom UA String'
    }

Auto Rotating User-Agent (scrapy-fake-useragent)

Install required packages:

pip install scrapy-fake-useragent fake-useragent faker


In settings.py:

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,
}

FAKEUSERAGENT_PROVIDERS = [
    'scrapy_fake_useragent.providers.FakeUserAgentProvider',
    'scrapy_fake_useragent.providers.FakerProvider',
]

RANDOM_UA_TYPE = 'random'  # Options: 'chrome', 'firefox', etc.


Run your spider and observe varying User-Agent headers in the logs.

Configuring Proxies

Proxies rotate IPs to bypass rate limits or bans.

Install Rotating Proxies:

pip install scrapy-rotating-proxies


Setup in settings.py:

DOWNLOADER_MIDDLEWARES.update({
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
})

ROTATING_PROXY_LIST_PATH = 'proxies.txt'  # Or ROTATING_PROXY_LIST = ['http://ip1:port', 'http://ip2:port']
ROTATING_PROXY_PAGE_RETRY_TIMES = 5
ROTATING_PROXY_BACKOFF_BASE = 300
ROTATING_PROXY_LOGSTATS_INTERVAL = 30


Create proxies.txt in the project root:

http://172.104.167.166:80
http://164.132.170.100:80
http://62.205.169.74:53281


Test proxies manually:

curl --proxy http://your_proxy https://httpbin.org/ip


Run the spider and monitor DEBUG logs for proxy assignments and bans.

Additional Tips

Ethical Scraping: ROBOTSTXT_OBEY = True, DOWNLOAD_DELAY = 3

Debugging: Use scrapy shell 'url' to test selectors interactively

JavaScript-heavy sites: Consider scrapy-playwright or scrapy-splash

Middleware issues: Ensure packages are installed and middleware order is correct

Useful Commands
# Open Scrapy shell
scrapy shell "https://www.scrapethissite.com/pages/forms/"

# Run spider and save JSON
scrapy crawl hockey -O output.json

# Show installed package versions
pip show scrapy
pip show scrapy-fake-useragent
pip show scrapy-rotating-proxies