# The classifier takes two lists of labels extracted by the labeler and decided whether they belong to the same news story or not.
# TODO:
# - figure out a good weight assignment
# - keep track of scores output by textrazor

import math

class Classifier():

    topicsWeight = 0.1

    def __init__(self):
        pass

    def getSimilarityScore(self, dict1, dict2):

        s = 0
        for topic1 in dict1['topics']:
            for topic2 in dict2['topics']:
                if(topic1 == topic2):
                    s += self.topicsWeight   # multiply by topic confidence score

        l = len(dict1['topics'])
        s = s / (l * (self.topicsWeight))       # normalize the scores
        return '%.3f'%(s)

    def setWeights(self, entWeight, topWeight):

        self.topicsWeight = topWeight
