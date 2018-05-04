# the database is a weighed undirected graph where each node is an article and the edge weights represent the "similarity score"
# between two articles (computed by the classifier)

<<<<<<< HEAD
# start by writing every function in pseudocode

import json, classifier

class Database():

    dict = {'Story':    {'StoryKeywords':[],
                            'ArticleIDs':[]
                                    'sID':0},
         'Articles':  {'ArticleKeywords':[],
                            'ArticleURL':[],
                                   'aID':0} }
    weightMatrix = []

    def __init__ (self):
        pass

# addArticle(Article1)
# if database contains no stories:
#     for article in database['Articles']:
#         s = getSimilarityScore(article.ArticleKeywords, Article1.ArticleKeywords)    # could also take articles as arguments
#         weightMatrix[article.ID][Article1.ID] = s
#         weightMatrix[Article1.ID][article.ID] = s  # for symmetry
#         database['Articles'].append(Article1)
# else
#     for story in database['Story']:
#         s = getSimilarityScore(story.StoryKeywords, Article1.StoryKeywords)    # could make story and article inherit from one class
#         if (s > threshold):    # or article passes rule that we chose to select stories in the first place
#             database['Articles'].append(Article1)
#             database['Story']['ArticleIDs'].append(Article1.aID)

# findArticle(Article2)
# for story in database['Story']:
#     
=======
class Story():

    def __init__(self):
        self.listOfKeyWords = []
        self.listOfArticlesId = []
        self.id = 0


class Article():

    def __init__(self):
        self.listOfArticleKeyWord = []
        self.URL = ""
        self.id = 0


database = {'Story':[],
            'Articles':[]}

s1 = Story()
s2 = Story()
s1.id = 1
s2.id = 2
a1 = Article()
a2 = Article()
a1.id = 5
a2.id = 9
s1.listOfArticlesId.append(a1.id)
s1.listOfArticlesId.append(a2.id)



database['Story'].append(s1)
database['Story'].append(s2)
database['Articles'].append(a1)
database['Articles'].append(a2)

for val in database['Story']:
    if(val.id == 1):
        print(val.listOfArticlesId)
>>>>>>> bd5b6573c97f7686db2ad5aad4a96ded4d4d76b3
