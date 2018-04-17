# The labeler takes a url of a news article, extracts topics and entities from the text and writes them in a text file.

# To do:
# think about labeling multiple urls concurrently
# output labels directly to the classifier component without the need for a file

import textrazor

textrazor.api_key = "5634740d9e8d89a14374edaa305c207bd6eda5918bbe233634beb092"

class Labeler:

    howManyTopics = 15
    howManyEntities = 15


    def __init__(self):
        self.client = textrazor.TextRazor(extractors=["topics", "entities"])  #instance of TextRazor class
        self.list = []

    def extractAndPrint(self, url):
        self.response = self.client.analyze_url(url)

        self.list.append("#TOPICS")
        for topic in self.response.topics()[1:self.howManyTopics]:
            self.list.append(topic.label)
        self.list.append("#ENTITIES")

        for entity in self.response.entities()[1:self.howManyEntities]:
            self.list.append(entity.id)
        self.list.append("#END")

        return self.list
