import SearchRSS
import feedparser
import io

from urllib3 import exceptions
from itertools import islice

class Pars:
    def __init__(self, rss):
        self.__rss = rss
        self.__limit = 1
        #self.Title()
        return None

    '''We only need one latest news article. Hence 'self.__limit' '''
    def Parsed(self):
        # name = Name of the outlet; title = Title of the article; link = link to the article
        return {'name': feedparser.parse(url_file_stream_or_string=self.__rss)['feed']['title'],
                'title': ''.join(Title.title for Title in islice(feedparser.parse(url_file_stream_or_string=self.__rss)['entries'], 1)), # Title of the Article,
                'link': ''.join(url.href for link in islice(feedparser.parse(url_file_stream_or_string=self.__rss)['entries'], 1) for url in islice(link.links, 1))
                }
    #TODO: Return description of article but I won't do that as it kind of gives it away

'''Feed homepage url to to search for an RSS then return one content'''
def GetRSSUrl(homepage):
    rss_url = SearchRSS.FeedSearch(homepage).RSS_Url()
    print('rss_url = {}'.format(rss_url))
    if rss_url != 'No RSS feed in {}'.format(homepage):
        return Pars(rss_url).Parsed()

'''Or feed rss urls to fetch recent articles
E.g https://www.courthousenews.com/feed/ or https://foreignpolicy.com/atom.xml'''
def FeedRSS(rss_url):
    return 'Outlet: {}\nArticle: {}\nLink: {}\n\n'.format(Pars(rss_url).Parsed()['name'], Pars(rss_url).Parsed()['title'], Pars(rss_url).Parsed()['link'])

"""This project was meant to iterate through multiple news articles."""
for feed in io.open('EveryNews', 'r').read().split():
    if feed.__contains__('http') and not None:
        try:
            print('Outlet: {}\nArticle: {}\nLink: {}\n\n'.format(GetRSSUrl(feed)['name'], GetRSSUrl(feed)['title'], GetRSSUrl(feed)['link']))
            #print(FeedRSS(feed))
        except TypeError:
            continue
