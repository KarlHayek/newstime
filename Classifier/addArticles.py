from pymongo import MongoClient
import labeler, classifier, database
labeler = labeler.Labeler()
db = database.Database()


def addArticles(links):
    waitlistedArticles = []
    for link in links:
        # feed the link to textrazor and make an article object from it
        article = labeler.extractIntoArticle(link)
        if len(article['topics']) == 0:
            print("Error:", link, "returned 0 topics"); continue

        # add the article to the articles collection
        article_id = db.insertArticle(article)

        # print("Now dealing with", article['title'], "...")
        foundAtLeastOneTimeline = False
        for timeline in db.timelines.find():
            # compare the article's topics to timeline's topics
            similarity = classifier.getSimilarityScore(article['topics'], timeline['topics'])
            print(similarity)

            # if the correlation is high enough, add the article to the timeline
            if similarity > 0.34:   # magic number
                print("ADDED", article['title'], ' TO TIMELINE ', timeline['title'])
                timeline['articles'].append(article_id)
                # update the timeline's topics from all of its articles
                timeline['topics'] = classifier.getTimelineTopicsFromArticles(db.getArticlesFromTimeline(timeline))

                db.updateTimeline(timeline)
                foundAtLeastOneTimeline = True
        
        # add an article to the waitlist if it wasn't added to any timeline
        if foundAtLeastOneTimeline == False:
            article['waitlisted'] = True
            article['waitlist_TTL'] = 5
            db.updateArticle(article)
            waitlistedArticles.append(article)
            print("WAITLISTED ARTICLE", article['title'])

    # handle the waitlist
    if len(waitlistedArticles) > 0:
        print("\nNow handling the waitlist...")

        addedTimelines, addeddArticles, removedArticles = classifier.handleWaitlistArticles(db.getWaitlistedArticles())
        # insert the clustered timelines and update the added articles (remove from waitlist)
        for timeline in addedTimelines: db.insertTimeline(timeline)
        for article in addeddArticles: db.updateArticle(article)
        for article in removedArticles: db.removeArticle(article)



# articles to add
links = [
    # "http://money.cnn.com/2018/03/21/technology/mark-zuckerberg-cambridge-analytica-response/index.html",
    # "https://www.usatoday.com/story/tech/2018/03/21/facebook-ceo-mark-zuckerberg-finally-speaks-cambridge-analytica-we-need-fix-breach-trust/445791002/",
    # "https://www.cnbc.com/2018/03/16/facebook-bans-cambridge-analytica.html",
    # "https://www.theguardian.com/uk-news/2018/mar/31/catalan-carla-ponsati-crowdfunding-scotland-spain",
    # "https://www.theguardian.com/world/2018/may/09/iran-fires-20-rockets-syria-golan-heights-israel",
    # "https://edition.cnn.com/2018/05/11/middleeast/iran-israel-syria-intl/index.html",
    # "https://www.nytimes.com/2018/05/13/world/middleeast/iran-nuclear-mideast-conflict.html",
    # "https://www.cnn.com/2018/05/14/politics/donald-trump-mueller-probe/index.html"
]
# addArticles(links)