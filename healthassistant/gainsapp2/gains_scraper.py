from bs4 import BeautifulSoup
import urllib2
import scrapy
from pymongo import MongoClient

class GainsSpider(scrapy.Spider):
    name = 'gainsspider'
    start_urls = ['https://www.bodybuilding.com/category/training']

    def parse(self, response):
        client = MongoClient()
        db = client.test
        current_site = 'https://www.bodybuilding.com/category/training'
        try:
            url = urllib2.urlopen(current_site).read()
        except:
            return
        article_dict = dict()
        article_info = []
        soup = BeautifulSoup(url, 'html.parser')
        article_titles = soup.findAll('span',{'class':'title'})
        count = 0
        for tag in article_titles:
            article_info.append(tag.string)
            link = tag.find('a')
            try:
                article_info.append(link['href'])
                article_dict.update({ '{}{}'.format('title', count):article_info[0]})
                article_dict.update({ '{}{}'.format('urls', count):article_info[1]})
                count = count + 1
                article_info = []
            except:
                pass
        db.insert_one(article_dict)
        yield article_dict
