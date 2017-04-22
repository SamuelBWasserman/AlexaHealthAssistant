from urllib.request import urlopen
from bs4 import BeautifulSoup


def scrape():
    current_site = 'https://www.bodybuilding.com/category/training'
    try:
        url = urlopen(current_site).read()
    except:
        return
    article_dict = dict()
    article_info = []
    soup = BeautifulSoup(url, 'html.parser')
    article_titles = soup.findAll('span',{'class':'title'})
    for tag in article_titles:
        article_info.append(tag.string)
        link = tag.find('a')
        try:
            article_info.append(link['href'])
        except:
            pass
        article_dict.update({article_info[1]:article_info[0]})
        article_info = []
    yield article_dict
