from pymongo import MongoClient

class Database:
    def __init__(self, environment='local'):
        # connect to local database
        if environment == 'local':
            self.db = MongoClient('mongodb://localhost:27017')['newstime-dev']
        # connect to production database
        elif environment == 'production':
            self.db = MongoClient('mongodb://ds129428.mlab.com:29428/')['newstime-prd']
            self.db.authenticate('karl', 'karl') # username and passw
        else:
            print("Error: database environment must either be local or production!")
            return
            
        self.articles = self.db.articles
        self.timelines = self.db.timelines

    def getArticlesFromTimeline(self, timeline):
        return self.articles.find({'_id': {'$in': timeline['articles']}})

    def getWaitlistedArticles(self):
        return self.articles.find({'waitlisted': True})

    def insertTimeline(self, timeline):
        return self.timelines.insert_one(timeline).inserted_id

    def insertArticle(self, article):
        return self.articles.insert_one(article).inserted_id

    def updateTimeline(self, timeline):
        self.timelines.update_one({'_id': timeline['_id']}, {"$set": timeline}, upsert=False)
    
    def updateArticle(self, article):
        self.articles.update_one({'_id': article['_id']}, {"$set": article}, upsert=False)

    def isArticleInDatabase(self, link):
        # find instead of find_one to get a cursor instead of a document, and limit to 1 result to improve performance
        return self.articles.find({'link': link}).limit(1).count() > 0

    def removeArticle(self, article):
        self.articles.remove({'_id': article['_id']})

    def cleanCollections(self):
        self.articles.remove({})
        self.timelines.remove({})

