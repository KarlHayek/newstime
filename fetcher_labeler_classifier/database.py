# the database is a weighed undirected graph where each node is an article and the edge weights represent the "similarity score"
# between two articles (computed by the classifier)

#TODO
# - find a way to select the story's keywords from the article keywords
# - fix and test 'add article to story'

import json, classifier, pprint

class Story():

    def __init__(self, keywordsDict = []):
        self.storyKeywords = keywordsDict       # most frequent keywords among article keywords
        self.articles = []                  # list of articles that belong to the story
        self.id = 0

class Article():

    def __init__(self, keywordsDict, url = ""):
        self.articleKeywords = keywordsDict         # keywords output by the labeler including article url)
        self.index = 0                          # unique number that identifies article

class Database():
    db = {'Stories':[],
         'Articles':[],
         'WaitList':[]}

    weightMatrix = []
    maxIndex = 0

    def __init__ (self):
        pass

    def printMatrix(self):
        for i in self.weightMatrix:
            print(i)

    def addArticle(self, newArticle):           # adds an instance of Article to the DB, updates the weightMatrix accordingly
        Clas = classifier.Classifier()
        self.db['Articles'].append(newArticle)
        newArticle.index = self.maxIndex
        self.maxIndex += 1
        newRow = []
        count = 0

        if(not bool(self.db['Stories'])):      # if there are no stories, put the article in the waitlist and update the weightMatrix
            self.db['WaitList'].append(newArticle)
            for art in self.db['Articles']:
                if(art == newArticle):
                    newRow.append(0)
                else:                           # find the similarity score between the new article and every other article
                    newRow.append(Clas.getSimilarityScore(newArticle.articleKeywords, art.articleKeywords))
                if(len(self.weightMatrix) > 0 and count < len(self.weightMatrix)):
                    self.weightMatrix[count].append(newRow[count])
                    count += 1
            self.weightMatrix.append(newRow)

        # else:
        #     maxSimilarity = 0
        #     bestStory = Story()
        #
        #     for story in self.db['Stories']:
        #         s = Clas.getSimilarityScore(story.storyKeywords, newArticle.articleKeywords)
        #         if(s > maxSimilarity):
        #             maxSimilarity = s
        #             bestStory = story
        #     bestStory.articlesList.append(newArticle)    # add the article to the story with which it has highest keyword similarity
        #
        #     for art in bestStory.articlesList:
        #         for i in range(len(self.weightMatrix)):
        #             if(i == art.index):               # fill in similarity score only for articles inside the story
        #                 newRow.append(Clas.getSimilarityScore(newArticle.articleKeywords, art.articleKeywords))
        #             else:
        #                 newRow.append(0)
        #             self.weightMatrix[i].append(newRow[i])
        #     newRow.append(0)
        #     self.weightMatrix.append(newRow)


    def search(self, keywordList):

        tempList = {'topics':keywordList}
        bestStory = Story()

        for story in db['Stories']:
            s = classifier.Classifier.getSimilarityScore(story.storyKeywords, tempList)
            if(s > maxSimilarity):
                maxSimilarity = s
                bestStory = story

        return bestStory

    def removeWeakEdges(self, threshold):  # removes all edges (sets weightMatrix entries to zero) in the waitlist that are less than threshold
        sparseMatrix = self.weightMatrix
        for art1 in self.db['WaitList']:
            for art2 in self.db['WaitList']:
                if (sparseMatrix[art1.index][art2.index] < threshold):
                    sparseMatrix[art1.index][art2.index] = 0;
        return sparseMatrix



# this enables a new article that has been fetched and labeled to be added to the database. addArticle takes a dict of article format.
# article format: article1 = {'keywords':[],
#                                   'ID': ""}
# the format will be changed, probably to add a "date" element later on for timeline sorting.
# If a new article is similar to a story it is added to it. if there are no stories yet, a similarity score is computed between the new article
# and all existing articles. if there are stories, but the new article belongs to none of them, it is added to the 'waitlist'. The rule
# that governs which articles belong together in a story should be exclusive enough that the waitlist never shrinks to zero, and generous
# enough that there is always a healthy amount of stories.

# addArticle(Article1)
# database['Articles'].append(Article1)   # add Article1 to the database
# if database contains no stories:
#     for article in database['Articles']:
#         s = getSimilarityScore(article.ArticleKeywords, Article1.ArticleKeywords)    # could also take articles as arguments
#         weightMatrix[article.ID][Article1.ID] = s
#         weightMatrix[Article1.ID][article.ID] = s  # for symmetry
# else
#     for story in database['Stories']:
#         s = getSimilarityScore(story.StoryKeywords, Article1.StoryKeywords)    # could make story and article inherit from one class
#         if (Article1 verifies rule to belong to story)
#             database['Stories']['ArticleIDs'].append(Article1.aID)    # make Article1 part of the story
#             for article in database['Stories'][this story's index]:
#                 s = getSimilarityScore(article.ArticleKeywords, Article1.StoryKeywords)    # compute similarity score with internal articles
#                 weightMatrix[article.ID][Article1.ID] = s
#                 weightMatrix[Article1.ID][article.ID] = s  # for symmetry
#     updateStories()    # articles with low relevance to the story are discarded



# this enables a user to search the db by providing a list of keywords. the classifier is used to judge whether the input list is sufficiently
# similar to some story's list of keywords, in which case it is returned and displayed on the timeline. This could be made more efficient by
# sorting the stories alphabetically. The waitlist is not searched.

# search(listOfKeywords)
# for story in database['Stories']:
#     s = getSimilarityScore(listOfKeywords, story.keywords)
#     if (s > searchThreshold):    # different threshold for searching, comparing articles together and comparing articles with stories.
#         return story



# this is called every time a new article is added to the db. it eliminates articles that aren't relevant to their stories. The article
# membership rule should be cheap enough so that looping through all articles to update isn't as bad as comparing keywords (which
# is O(|keywords|^2)). Also, articles in the waitList are compared to the updated stories to see if they belong in some of them, and
# among each other to see if they could form a new story. That way stories grow organically, they aren't determined by a rigid rule.

# updateStories()
# for story in database['Stories']:     # removes irrelevant articles from existing stories and sends them to the waitList
#     for article in story:
#         if article doesn't verify rule anymore:
#             story['ArticleIDs'].remove(article.ID)    # donno how this will be done
#             waitList.append(article)
# for article in waitList:              # tries to create stories from articles in the waitList
#     apply rule to group articles into a story
# for article in waitlist:              # those that weren't grouped into a new story try to find an existing story to join
#     for story in database['Stories']:
#         if (Article1 verifies rule to belong to story)     # articles with 15 largest pageRanks
#             database['Stories']['ArticleIDs'].append(Article1.aID)    # make Article1 part of the story
#             for article in database['Stories'][this story's index]:
#                 s = getSimilarityScore(article.ArticleKeywords, Article1.StoryKeywords)    # compute similarity score with internal articles
#                 weightMatrix[article.ID][Article1.ID] = s
#                 weightMatrix[Article1.ID][article.ID] = s  # for symmetry
#
# read about centrality metrics for networks to decide how to group articles into stories. try pageRank.

#
