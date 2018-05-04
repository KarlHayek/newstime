import labeler
import classifier
import json


# l1 = labeler.Labeler()
# list1 = l1.extractIntoList("http://money.cnn.com/2018/03/21/technology/mark-zuckerberg-cambridge-analytica-response/index.html")
# print(list1)
# print("\n")
#
# l1.printJSON()

database = {'Story': {'StoryKeywords':[],
                         'ArticleIDs':[]},
         'Articles': {'ArticleKeywords':[],
                        'ArticleURL':[]}}

storyKeywordsList = []
storyKeywordsList.extend(("mexico", "wall", "trump"))

articleIDList = []
articleIDList = [1,7,3,67]

articleKeywordsList = []
articleKeywordsList.extend(("mexico", "l'amour"))

articleURL = "www.fairelamourtoutseul.com"

database['Story']['StoryKeywords'].append(storyKeywordsList)
database['Story']['ArticleIDs'].append(articleIDList)
database['Articles']['ArticleKeywords'].append(articleKeywordsList)
database['Articles']['ArticleURL'].append(articleURL)

with open('labels.json', 'w') as outfile:
    json.dump(database, outfile)
print (json.dumps(database, indent=4))
