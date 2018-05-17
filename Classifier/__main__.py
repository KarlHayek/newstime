import sys, database, feedParser, labeler, classifier, addArticle

# links to add manually
manualLinks = [
    # "http://money.cnn.com/2018/03/21/technology/mark-zuckerberg-cambridge-analytica-response/index.html",
    # "https://www.usatoday.com/story/tech/2018/03/21/facebook-ceo-mark-zuckerberg-finally-speaks-cambridge-analytica-we-need-fix-breach-trust/445791002/",
    # "https://www.theguardian.com/world/2018/may/09/iran-fires-20-rockets-syria-golan-heights-israel",
    # "https://edition.cnn.com/2018/05/11/middleeast/iran-israel-syria-intl/index.html",
    # "https://www.nytimes.com/2018/05/13/world/middleeast/iran-nuclear-mideast-conflict.html",
    # "https://www.cnn.com/2018/05/14/politics/donald-trump-mueller-probe/index.html"
]


def main(visualize = False):
    print("Fetching article links from RSS feeds...")
    linksToAdd = feedParser.getLinksFromRSS(db) if len(manualLinks) == 0 else manualLinks

    print("\nExtracting articles from links and handling them...\n")
    nbWaitlistedArticles = 0
    for link in linksToAdd:
        # feed the link to textrazor and make an article object from it
        article = labeler.extractIntoArticle(link)
        if len(article['topics']) == 0:
            print("Error:", link, "returned 0 topics"); continue

        nbWaitlistedArticles += addArticle.addArticle(article, db)

    # if at least 1 article was added to the waitlist, handle all waitlisted articles in the database
    if nbWaitlistedArticles > 0:
        print("\nNow handling the waitlist...")

        addedTimelines, addeddArticles, removedArticles = classifier.handleWaitlistArticles(db.getWaitlistedArticles(), visualize)
        # insert the clustered timelines, update articles added to timeilnes and remove them from waitlist
        for timeline in addedTimelines: db.insertTimeline(timeline)
        for article in addeddArticles: db.updateArticle(article)
        for article in removedArticles: db.removeArticle(article)
    print("\nDone")




def populateInitDatabase():
    articleLinksPerTimeline = [
        [   "https://www.cnn.com/2018/05/12/politics/washington-lobbying-trump-era/index.html",
            "https://www.theguardian.com/world/2018/may/13/us-sanctions-european-countries-iran-deal-donald-trump",
            "https://www.theatlantic.com/magazine/archive/2017/10/will-donald-trump-destroy-the-presidency/537921/",
        ],
        [   "https://www.vox.com/policy-and-politics/2018/4/11/17225518/mark-zuckerberg-testimony-facebook-privacy-settings-sharing",
            "https://www.wired.com/story/mark-zuckerberg-plays-the-scapegoat-for-our-facebook-sins",
            "https://www.telegraph.co.uk/technology/2018/04/17/facebook-quietly-stopped-apps-harvesting-users-private-data",
        ]]
    newTimelines = [
        { 'title': "Donald Trump Presidency", 'details': "Events related to President Drumpf's presidency" },
        { 'title': "The Zucc", 'details': "The adventures of Marc Zuckerberg" }
    ]

    print("Initializing database...")
    db.cleanCollections()
    for i, timeline in enumerate(newTimelines):
        timeline["articles"] = []

        # go over the timeline's articles
        for link in articleLinksPerTimeline[i]:
            article = labeler.extractIntoArticle(link)      # feed the link to textrazor and make an article object from it
            article_id = db.insertArticle(article)          # add the article to the articles collection
            timeline["articles"].append(article_id)         # add the article's id to the timeline's list of articles

        articles = db.getArticlesFromTimeline(timeline)     # get the timeline's articles
        timeline["topics"] = classifier.getTimelineTopicsFromArticles(articles)     # set the timeline's topics from its articles
        db.insertTimeline(timeline)                         # add the timeline to the timelines collection
    print("Done initializing database")
    




if __name__ == "__main__":
    db = database.Database("local")
    labeler = labeler.Labeler()
    
    if len(sys.argv) > 1 and sys.argv[1].lower() in "initialize":
        populateInitDatabase()
    elif len(sys.argv) > 1 and sys.argv[1].lower() in "visualize":
        main(visualize = True)
    else:   main()