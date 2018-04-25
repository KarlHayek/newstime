import labeler
import classifier
import json


l1 = labeler.Labeler()
list1 = l1.extractIntoList("http://money.cnn.com/2018/03/21/technology/mark-zuckerberg-cambridge-analytica-response/index.html")
print(list1)
print("\n")

l1.printJSON()



# l2 = labeler.Labeler()
# list2 = l2.extractAndPrint("https://www.nytimes.com/2018/03/27/world/europe/whistle-blower-data-mining-cambridge-analytica.html")
# print(list2)
# print("\n")
#
# c1 = classifier.Classifier()
# c1.readAndCompare(list1, list2)
