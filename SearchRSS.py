from feedfinder2 import find_feeds
from feedsearch import url

class FeedSearch: # Return the RSS Feed url from the given webpage
    '''
    Fetches and returns the RSS, or feed, url. Will return true if the url is feed like.
    How it works? Feed the FeedSearch class with a homepage url of a news article. It will then crawl to find the url feed.
    E.g [
    import SearchRSS
    rssUrl = SearchRSS.FeedSearch('https://www.courthousenews.com/').RSS_Url()
    >>https://www.courthousenews.com/feed/
    ]
    '''
    def __init__(self, site: str):
        self.__site = site

        # Check if that url is RSS feed like first. Otherwise, crawl and find possible feed like urls. Returns as list
        self.__getLink = self.__site if url.URL.is_feedlike_url(self.__site) != False else find_feeds(self.__site, check_all=False, user_agent=None)
        return None

    def RSS_Url(self):
        '''Checks if url is feed like (contains RSS, XML, JSON, etc)'''
        #self.rss = [f for f in self.__findRSS][0]
        try:
            if type(self.__getLink) is list:
                #if url.URL.is_feedlike_url([f for f in self.__getLink][0]) == True:
                return [uri for uri in self.__getLink][0] if [uri for uri in self.__getLink][0] != str(None) else 'Could be possible that there may not be an RSS feed in ' + str(self.__site)
            elif type(self.__getLink) is not list:
                return self.__getLink
        except IndexError:
            return 'No RSS feed in {}'.format(self.__site)

if __name__ == '__main__':
    print(FeedSearch('https://www.couthousenews.com/').RSS_Url())
