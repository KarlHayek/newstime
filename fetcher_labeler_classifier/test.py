import labeler
import classifier
import json


# l1 = labeler.Labeler()
# list1 = l1.extractIntoList("http://money.cnn.com/2018/03/21/technology/mark-zuckerberg-cambridge-analytica-response/index.html")
# print(list1)
# print("\n")
#
# l1.printJSON()

# created some dicts
database = {'Stories':[],
           'Articles':[]}

story1 = {'keywords':[],    # these are instances of dicts, not declarations
       'articleIDs':[],
               'ID': ""}

article1 = {'keywords':[],
                 'ID': ""}

# saw if i could append lists and strings to the dicts, turns out i can
storyKeywordsList = []
storyKeywordsList.extend(("mexico", "wall", "trump"))

articleIDList = []
articleIDList = [1,7,3,67]

articleKeywordsList = []
articleKeywordsList.extend(("mexico", "l'amour"))

articleURL = "www.fairelamourtoutseul.com"

story1['keywords'].append(storyKeywordsList)
story1['articleIDs'].append(articleIDList)
story1['ID'] = 20

# created another "instance of a story" (although there is no 'story' abstraction in the code, only in our imagination)
story2 = {'keywords':["frank"],
        'articleIDs':[1,2,3],
                'ID': "21"}

database['Stories'].append(story1)
database['Stories'].append(story2)

database['Stories'][1]['keywords'] = "farid"        # uf!

print(database['Stories'])

# with open('labels.json', 'w') as outfile:
#     json.dump(database, outfile)
# print (json.dumps(database, indent=4))
