import scrapy
from bs4 import BeautifulSoup
import urllib2


class QuotesSpider(scrapy.Spider):
    name = "gains"

    def start_requests(self):
        urls = [
            'https://www.bodybuilding.com/category/training',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        current_site = response.url
        try:
            url = urllib2.urlopen(current_site).read()
        except:
            return
        soup = BeautifulSoup(url, 'html.parser')
        articles = soup.findAll('span',{'class':'title'})
        for tag in articles:
            print(tag.string)
