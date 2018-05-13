from pymongo import MongoClient
import labeler, classifier
labeler = labeler.Labeler()

# connect to local database
db = MongoClient('mongodb://localhost:27017')['newstime-dev']
# connect to production database
# db = MongoClient('mongodb://karl:karl@ds129428.mlab.com:29428')['newstime-prd')  


# articles to add
links = [
    "http://money.cnn.com/2018/03/21/technology/mark-zuckerberg-cambridge-analytica-response/index.html",
    # "https://www.usatoday.com/story/tech/2018/03/21/facebook-ceo-mark-zuckerberg-finally-speaks-cambridge-analytica-we-need-fix-breach-trust/445791002/",
    # "https://www.theguardian.com/world/2018/may/09/iran-fires-20-rockets-syria-golan-heights-israel",
    # "https://www.theguardian.com/uk-news/2018/mar/31/catalan-carla-ponsati-crowdfunding-scotland-spain",
    # "https://edition.cnn.com/2018/05/11/middleeast/iran-israel-syria-intl/index.html",
    # "https://www.cnbc.com/2018/03/16/facebook-bans-cambridge-analytica.html"
]

for link in links:
    # feed the link to textrazor and make an article object from it
    article = labeler.extractIntoArticle(link)


    # # insert the article in the database
    # article_id = db.articles.insert_one(article).inserted_id

    # for timeline in db.timelines.find():
    #     ## compare the article's labels to timeline's
    #     #...

    #     #if the correlation is high enough, add the article to the timeline
    #     if 1:
    #         timeline['articles'].append(article_id)
    #         db.timelines.update_one({'_id': timeline['_id']}, {
    #                                 "$set": timeline}, upsert=False)
