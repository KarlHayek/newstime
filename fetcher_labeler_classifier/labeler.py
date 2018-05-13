# The labeler takes a url of a news article, extracts topics from the text and writes them in a text file.

import textrazor, json, database, pprint

textrazor.api_key = "5634740d9e8d89a14374edaa305c207bd6eda5918bbe233634beb092"

class Labeler:

    howManyTopics = 40

    def __init__(self):
        self.client = textrazor.TextRazor(extractors=["topics"])  #instance of TextRazor class

    def extractIntoArticle(self, url):

        dict = {
            'topics':[],
            'link': ""
        }

        self.response = self.client.analyze_url(url)

        for topic in self.response.topics()[1:self.howManyTopics]:
            dict['topics'].append(topic.label)

        dict['link'] = url

        art = database.Article(dict)
        return art

    def printJSON(self):

        with open('labels.json', 'w') as outfile:
            json.dump(self.dict, outfile)
        print (json.dumps(self.dict, indent=4, sort_keys=True))


# pair enumerator component, enumerates pairs or urls from a list, do function that could be "do", and a function that only enumerates
# this can be used also to compare keywords: separation of concerns. rewriting the thing is refactoring

# work on sorting by time (temporal entity extraction, normalization, ordering). use article writing time as reference
# tell other subteam to talk to prof

# use software connectors between javascript and python. you need a system connection, or a network connection, or a file (te3tir)
