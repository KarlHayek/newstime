# the database is a weighed undirected graph where each node is an article and the edge weights represent the "similarity score"
# between two articles (computed by the classifier)

class Story():

    def __init__(self):
        self.listOfKeyWords = []
        self.listOfArticlesId = []
        self.id = 0


class Article():

    def __init__(self):
        self.listOfArticleKeyWord = []
        self.URL = ""
        self.id = 0


database = {'Story':[],
            'Articles':[]}

s1 = Story()
s2 = Story()
s1.id = 1
s2.id = 2
a1 = Article()
a2 = Article()
a1.id = 5
a2.id = 9
s1.listOfArticlesId.append(a1.id)
s1.listOfArticlesId.append(a2.id)



database['Story'].append(s1)
database['Story'].append(s2)
database['Articles'].append(a1)
database['Articles'].append(a2)

for val in database['Story']:
    if(val.id == 1):
        print(val.listOfArticlesId)
