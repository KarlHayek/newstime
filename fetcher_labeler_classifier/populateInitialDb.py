from pymongo import MongoClient
import labeler, classifier
labeler = labeler.Labeler()

# connect to local database
db = MongoClient('mongodb://localhost:27017')['newstime-dev']
# connect to production database
# db = MongoClient('mongodb://karl:karl@ds129428.mlab.com:29428')['newstime-prd')

articleLinksPerTimeline = [
    [
        "https://www.washingtontimes.com/news/2018/apr/12/donald-trumps-wall-is-getting-push-back-from-congr/",
        "https://www.cnn.com/2018/05/12/politics/washington-lobbying-trump-era/index.html"
    ],
    [
        "https://www.vox.com/policy-and-politics/2018/4/11/17225518/mark-zuckerberg-testimony-facebook-privacy-settings-sharing"
    ]
]

newTimelines = [
    {
        'title': "Trump Wall",
        'details': "Events related to the wall that President Trump wants to erect in the US-Mexico border"
    },
    {
        'title': "The Zucc",
        'details': "The adventures Marc Zuckerberg"
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
    
    # set the timeline's topics from its articles
    timeline["topics"] = classifier.getTimelineTopicsFromArticles(timeline)

    # add the timeline to the timelines collection
    db.timelines.insert_one(timeline)
    print("finished timeline", index)
    index+=1

print("Done")
