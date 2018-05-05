# the database is a weighed undirected graph where each node is an article and the edge weights represent the "similarity score"
# between two articles (computed by the classifier)

# start by writing every function in pseudocode

import json, classifier

# class Story():
#
#     def __init__(self):
#         self.storyKeywords = []
#         self.articleIDs = []
#         self.id = 0
#
#
# class Article():
#
#     def __init__(self):
#         self.articleKeywords = []
#         self.articleURL = ""
#         self.id = 0


class Database():

    db = {'Stories':[],
         'Articles':[],
         'WaitList':[]}

    weightMatrix = []

    def __init__ (self):
        pass

# this enables a new article that has been fetched and labeled to be added to the database. addArticle takes a dict of article format.
# article format: article1 = {'keywords':[],
#                                   'ID': ""}
# the format will be changed, probably to add a "time" element later on for timeline sorting.
# A new article is similar to a story it is added to it. if there are no stories yet, a similarity score if computed between the new article
# and all existing articles. if there are stories, but the new article belongs to none of them, it is added to the 'waitlist'.

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
#     if (s > threshold):
#         return story



# this is called every time a new article is added to the db. it changes the articles that belong to each story based on their new relevance
# and eliminates articles that aren't relevant to their stories. The article membership rule should be cheap enough so that looping through
# all articles to update isn't as bad as comparing keywords (which itself is O(|keywords|^2)). Articles in the waitlist are compared to the
# updated stories to see if they belong in some of them.

# updateStories()
# for story in database['Stories']:
#     for article in story:
#         if article doesn't verify rule anymore:
#             story['ArticleIDs'].remove(article.ID)    # donno how this will be done
#             waitList.append(article)
# for article in waitList:
#     apply rule to group articles into a story
# for article in waitlist:    # those that weren't grouped into a new story
#     for story in database['Stories']:
#         if (Article1 verifies rule to belong to story)
#             database['Stories']['ArticleIDs'].append(Article1.aID)    # make Article1 part of the story
#             for article in database['Stories'][this story's index]:
#                 s = getSimilarityScore(article.ArticleKeywords, Article1.StoryKeywords)    # compute similarity score with internal articles
#                 weightMatrix[article.ID][Article1.ID] = s
#                 weightMatrix[Article1.ID][article.ID] = s  # for symmetry
#
#
