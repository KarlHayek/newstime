# The classifier takes two lists of labels extracted by the labeler and decided whether they belong to the same news story or not.
# TODO:
# - figure out a good weight assignment
# - keep track of scores output by textrazor

import math


topicsWeight = 0.1

def getSimilarityScore(topics_list1, topics_list2):

    s = 0
    for topic1 in topics_list1:
        for topic2 in topics_list2:
            if(topic1 == topic2):
                s += topicsWeight   # multiply by topic confidence score

    l = len(topics_list1)
    s = s / (l * (topicsWeight))       # normalize the scores
    return '%.3f'%(s)


def classifyTimelinefromArticles(timeline):
    print("ASD")