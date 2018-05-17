from feedparser import parse

def getLinksFromRSS(database):
    # Grabs the rss feed url's and return them as a list
    def getArticleLinks(rss_url):
        newsitems = parse(rss_url)['items']

        return [newsitem['link'] for newsitem in newsitems][:20] # 20 links per rss feed

    # List of RSS feeds that we will fetch and combine
    newsurls = {
        'googlenews':       'https://news.google.com/news/rss/?hl=en&amp;ned=us&amp;gl=US',
        'yahoonews':        'http://news.yahoo.com/rss/'
    }

    allLinks = []
    # get links from all the feeds
    for key, rss_url in newsurls.items():
        allLinks.extend(getArticleLinks(rss_url))

    return [link for link in allLinks if not database.isArticleInDatabase(link)]