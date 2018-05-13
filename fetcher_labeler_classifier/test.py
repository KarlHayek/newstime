import labeler
import classifier
import database as db
import json


l1 = labeler.Labeler()
db1 = db.Database()

links = [
    "http://money.cnn.com/2018/03/21/technology/mark-zuckerberg-cambridge-analytica-response/index.html",
    "https://www.usatoday.com/story/tech/2018/03/21/facebook-ceo-mark-zuckerberg-finally-speaks-cambridge-analytica-we-need-fix-breach-trust/445791002/",
    "https://www.theguardian.com/world/2018/may/09/iran-fires-20-rockets-syria-golan-heights-israel",
    "https://www.theguardian.com/uk-news/2018/mar/31/catalan-carla-ponsati-crowdfunding-scotland-spain",
    "https://edition.cnn.com/2018/05/11/middleeast/iran-israel-syria-intl/index.html",
    "https://www.cnbc.com/2018/03/16/facebook-bans-cambridge-analytica.html"
]
for link in links:
    art = l1.extractIntoArticle(link)
    # print (art.articleKeywords["TOPICS"][0])
    db1.addArticle(art)


db1.printMatrix()

# with open('labels.json', 'w') as outfile:
#     json.dump(list1, outfile)
# print (json.dumps(list1, indent=4))
