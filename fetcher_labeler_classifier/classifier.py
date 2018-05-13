# The classifier takes two lists of labels extracted by the labeler and decided whether they belong to the same news story or not.

import math
from collections import OrderedDict

topicsWeight = 0.1

def getSimilarityScore(topics1, topics2, topic_scores1 = [], topic_scores2 = []):

    score = 0
    for topic1 in topics1:
        for topic2 in topics2:
            if(topic1 == topic2):
                score += topicsWeight   # multiply by topic confidence score

    l = len(topics1)
    score = score / (l * (topicsWeight))       # normalize the scores
    # return '%.3f'%(s)
    return score



def getTimelineTopicsFromArticles(articles):
    keywordRelevance = {}; size = 0

    for article in articles:
        for i in range(len(article['topics'])):
            # if the keyword hasn't been entered yet
            if (not article['topics'][i] in keywordRelevance):
                keywordRelevance[article['topics'][i]] = 0
            else:
                # increment frequency for 'keyword' 
                keywordRelevance[article['topics'][i]] += article['topic_scores'][i]
        size+=1

    # order by score
    ordered = OrderedDict(sorted(keywordRelevance.items(), key=lambda t: t[1], reverse=True))
    timelineTopics = []
    for keyword, relevance in ordered.items():
        if relevance > 0.2 * size:      # if the keyword appears in more than a certain fraction of the number of articles
            timelineTopics.append(keyword)

    return timelineTopics
