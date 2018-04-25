# The labeler takes a url of a news article, extracts topics and entities from the text and writes them in a text file.

# To do:
# think about labeling multiple urls concurrently
# output labels directly to the classifier component without the need for a file

import textrazor, json

textrazor.api_key = "5634740d9e8d89a14374edaa305c207bd6eda5918bbe233634beb092"

class Labeler:

    howManyTopics = 15
    howManyEntities = 15
    dict = {'TOPICS':[],
            'ENTITIES':[],
            'URL':[]}

    def __init__(self):
        self.client = textrazor.TextRazor(extractors=["topics", "entities"])  #instance of TextRazor class
        self.list = []

<<<<<<< HEAD

    def extractIntoList(self, url):
=======
    # Rev: what does "print" in the function name mean? The function doesn't print anything, it calls the textrazor api and extracts information from it.
    # Rev: self.list is a list of strings that contain the extracted information. It can be replaced with a single string Extract that contains all the information,
    # instead of a list of strings. Or even better, a dictionary can be used, which can then be easily written as a JSON file.
    def extractAndPrint(self, url):
>>>>>>> e5ab88419b4e00da8eb681ca2a757093e876cd41
        self.response = self.client.analyze_url(url)

        self.list.append("#TOPICS")
        for topic in self.response.topics()[1:self.howManyTopics]:
            self.list.append(topic.label)
            self.dict['TOPICS'].append(topic.label)
        self.list.append("#ENTITIES")

        for entity in self.response.entities()[1:self.howManyEntities]:
            self.list.append(entity.id)
            self.dict['ENTITIES'].append(entity.id)
        self.list.append("#END")
        self.dict['URL'].append(url)

        return self.list


    def printJSON(self):

        with open('labels.json', 'w') as outfile:
            json.dump(self.dict, outfile)
        print (json.dumps(self.dict, indent=4, sort_keys=True))


# pair enumerator component, enumerates pairs or urls from a list, do function that could be "do", and a function that only enumerates
# this can be used also to compare keywords: separation of concerns. rewriting the thing is refactoring

# work on sorting by time (temporal entity extraction, normalization, ordering). use article writing time as reference
# tell other subteam to talk to prof

# use software connectors between javascript and python. you need a system connection, or a network connection, or a file (te3tir)
