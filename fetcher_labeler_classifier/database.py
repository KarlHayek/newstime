# the database is a weighed undirected graph where each node is an article and the edge weights represent the "similarity score"
# between two articles (computed by the classifier)

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
