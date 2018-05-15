from pymongo import MongoClient
import labeler, classifier, database
labeler = labeler.Labeler()
db = database.Database()
db.cleanCollections()


articleLinksPerTimeline = [
    [
        "https://www.washingtontimes.com/news/2018/apr/12/donald-trumps-wall-is-getting-push-back-from-congr/",
        "https://www.cnn.com/2018/05/12/politics/washington-lobbying-trump-era/index.html",
        "https://www.theguardian.com/world/2018/may/13/us-sanctions-european-countries-iran-deal-donald-trump",
        "https://www.theatlantic.com/magazine/archive/2017/10/will-donald-trump-destroy-the-presidency/537921/",
    ],
    [
        "https://www.vox.com/policy-and-politics/2018/4/11/17225518/mark-zuckerberg-testimony-facebook-privacy-settings-sharing",
        "https://www.wired.com/story/mark-zuckerberg-plays-the-scapegoat-for-our-facebook-sins",
        "https://www.telegraph.co.uk/technology/2018/04/17/facebook-quietly-stopped-apps-harvesting-users-private-data",
    ]
]

newTimelines = [
    {
        'title': "Donald Trump Presidency",
        'details': "Events related to President Drumpf's presidency"
    },
    {
        'title': "The Zucc",
        'details': "The adventures of Marc Zuckerberg"
    }
]




index = 0
for timeline in newTimelines:
    timeline["articles"] = []

    # go over the timeline's articles
    for link in articleLinksPerTimeline[index]:
        # feed the link to textrazor and make an article object from it
        article = labeler.extractIntoArticle(link)

        # add the article to the articles collection
        article_id = db.articles.insert_one(article).inserted_id
        
        # add the article's id to the timeline's list of articles
        timeline["articles"].append(article_id)
    
    # get the timeline's articles
    articles = db.getArticlesFromTimeline(timeline)

    # set the timeline's topics from its articles
    timeline["topics"] = classifier.getTimelineTopicsFromArticles(articles)
    # print(timeline['topics'])

    # add the timeline to the timelines collection
    db.timelines.insert_one(timeline)
    print("finished timeline", index)
    index+=1

print("Done")

# tl = db.timelines.find_one()
# articles = db.articles.find({'_id': {'$in': tl['articles']}})
# topics = classifier.getTimelineTopicsFromArticles(articles)
# print(topics)
