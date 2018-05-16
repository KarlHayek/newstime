import feedparser, database, addArticles
db = database.Database()

def getLinksFromRSS():
    print("Fetching article links from RSS feeds...")
    # Grabs the rss feed url's and return them as a list
    def getArticleLinks(rss_url):
        newsitems = feedparser.parse(rss_url)['items']

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

    return [link for link in allLinks if not db.isArticleInDatabase(link)]


linksToAdd = getLinksFromRSS()

print("Now adding article links to database...")
# linksToAdd = linksToAdd[:10]  # don't add all the links, for testing
addArticles.addArticles(linksToAdd)
