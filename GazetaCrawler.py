# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 19:29:22 2016

@author: piotrgrudzien
"""

from Crawler import Crawler
from bs4 import Comment
from Logger import Logger


class GazetaCrawler(Crawler):
    def __init__(self):
        Crawler.__init__(self, 'http://wiadomosci.gazeta.pl/wiadomosci/0,0.html', 'Gazeta')

    def scrape_urls(self):
        print 'Scraping', self.name
        section = self.mainPage.find(id='holder_201')
        for link in section.find_all('a'):
            new_url = link.get('href')
            if (new_url.startswith('http://wiadomosci.gazeta.pl/wiadomosci/') and (new_url.endswith('.html')) and (
                    new_url not in self.timeline) and ('-' in new_url)):
                self.urls.append(new_url)

    def scrape_text(self, link):

        soup = self.read_page(link)

        self.title = soup.title.string

        self.bold = soup.find(id='gazeta_article_lead').get_text()

        first = True
        id_article = soup.find(id='artykul')

        if id_article is None:
            return

        for item in id_article.findAll(text=True, recursive=False):
            """ Ignore comments and empty strings """
            if(not isinstance(item, Comment)) or (not item):
                # self.body += item.encode('UTF8')
                self.body += item

# def gazetaCrawl():
#     print 'GAZETA CRAWL'
#
#     link = 'http://wiadomosci.gazeta.pl/wiadomosci/0,0.html'
#
#     """ Read the main gazeta wiadomosci page """
#     r = urllib2.urlopen(link).read()
#     soup = BeautifulSoup(r, 'lxml')
#
#     """ Find the sections where all the links are """
#     section = soup.find(id = 'holder_201')
#
#     """ Load the timeline from file """
#     try:
#         Gazeta_Timeline = pickle.load(open('../Gazeta/Gazeta_Timeline.p', 'rb'))
#     except IOError:
#         print 'Loading empty Gazeta_Timeline'
#         Gazeta_Timeline = {}
#
#     Gazeta_Urls = []
#
#     """ Get the links of the articles you haven't seen before """
#     """ Checking for '-' is ugly making sure it is an actual article """
#     for link in section.find_all('a'):
#         newUrl = link.get('href')
#         if(newUrl.startswith('http://wiadomosci.gazeta.pl/wiadomosci/') and (newUrl.endswith('.html')) and (newUrl not in Gazeta_Timeline) and ('-' in newUrl)):
#             Gazeta_Timeline[newUrl] = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
#             Gazeta_Urls.append(newUrl)
#
#     """ Pickle the updated timeline """
#     pickle.dump(Gazeta_Timeline, open("../Gazeta/Gazeta_Timeline.p", "wb"))
#
#     """ Get text of each article and write to file """
#     print 'Adding', len(Gazeta_Urls), 'articles'
#     for url in Gazeta_Urls:
#         r = urllib2.urlopen(url).read()
#         soup = BeautifulSoup(r, 'lxml')
#         print 'Link:', url
#         title = soup.title.string
#
#         f = open('../Gazeta/Articles/' + title + '.txt', 'w')
#
#         f.write('TITLE:' + removePunct(title.encode('UTF8')) + '\n')
#
#         bold = soup.find(id = 'gazeta_article_lead').get_text()
#         f.write('BOLD:' + removePunct(bold.encode('UTF8')) + '\n')
#
#         body = soup.find(id = 'artykul')
#
#         first = True
#         for item in body.findAll(text = True, recursive = False):
#             """ Ignore comments and empty strings """
#             if((not isinstance(item, Comment)) or (not item)):
#                 out = item.encode('UTF8')
#                 if(first):
#                     f.write('BODY:' + out)
#                     first = False
#                 else:
#                     f.write(out)
#         f.close()