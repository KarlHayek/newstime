# The classifier takes two lists of labels extracted by the labeler and decided whether they belong to the same news story or not.

# To do:
# - figure out a good weight assignment
# - !! false negatives are better than false positives !!

class Classifier():

    entitiesWeight = 3
    topicsWeight = 1
    score = 0
    scoreThreshold = 20

    def __init__(self):
        pass

    # Rev: Read JSON files instead of .txt files, for easier and faster access
    # Rev: From what I understood, this function takes as parameters two outputs from textrazor calls on differnet article links. The variable names should be made more clear.
    def readAndCompare(self, list1, list2):

        if (list1[0] != "#TOPICS"):
            print("wrong file1")
        if (list2[0] != "#TOPICS"):
            print("wrong file2")

        # Rev: this comparison is computationally expensive. Using JSON may help speed it up
        # scan topics to look for common words. #ENTITIES string signals end of topics sublist
        for line1 in list1:
            if(line1 == "#ENTITIES"):
                break
            for line2 in list2:
                if(line2 == "#ENTITIES"):
                    break
                if(line1 == line2):
                    self.score += self.entitiesWeight

        # scan entities to look for common words. #END string signals end of entities sublist
        for line1 in list1:
            if(line1 == "#END"):
                break
            for line2 in list2:
                if(line2 == "#END"):
                    break
                if(line1 == line2):
                    self.score += self.topicsWeight

        # update similarity score according to preset weights
        # if self.score > self.scoreThreshold:
        #     print("\n \n same story")
        # else:
        #     print("\n \n different story")
        # print("similarity score: ")
        return self.score

    def setWeights(self, entWeight, topWeight):
        self.entitiesWeight = entWeight
        self.topicsWeight = topWeight



# list1 = ["#TOPICS", "beer", "titties"]
# list2 = ["beer", "#TOPICS", "titties"]

# Rev: remove old code, it's useless

#############   OLD CODE   ###############

        # # file1 = open(filename1, "r")
        # # file2 = open(filename2, "r")
        #
        # # print(file1.readline())
        # # print(file2.readline())
        #
        # # compare entities
        # with open(filename1, "r") as file1:
        #     for line1 in file1:
        #         if(line1 == "#TOPICS"):
        #             print("f")


# file1 = open("labels1.txt", "r")
# file2 = open("labels2.txt", "r")
#
# print(file1.readline())
# print(file2.readline())


# while (file1.readline() != "#ENTITIES"):
#     while (file2.readline() != "#ENTITIES"):
#         if (file1.readline() == file2.readline()):
#             print(file1.readline())
#             score += entitiesWeight
#         file2.next()
#     file1.next()
#
# while (file1.readline() != "#END"):
#     while (file2.readline() != "#END"):
#         if (file1.readline() == file2.readline()):
#             print(file1.readline())
#             score += topicsWeight
#         file2.next()
#     file1.next()
#
# if self.score > self.scoreThreshold:
#     print("same story")
# else:
#     print("different story")
