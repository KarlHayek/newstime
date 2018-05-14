# The labeler takes a url of a news article, extracts topics from the text and writes them in a text file.

import textrazor, pprint
from bs4 import BeautifulSoup

textrazor.api_key = "5634740d9e8d89a14374edaa305c207bd6eda5918bbe233634beb092"

class Labeler:
    def __init__(self):
        self.client = textrazor.TextRazor(extractors=["topics"])  #instance of TextRazor class

    def extractIntoArticle(self, url):
        article = {
            'link': url,
            'title': self.getTitle(url),
            'topics':[],
            'topic_scores': [],
            'waitlisted': False,
        }

        self.response = self.client.analyze_url(url)

        for topic in self.response.topics():
            if topic.score < 0.4:   # magic number
                break   # don't add low-score topics
            article['topics'].append(topic.label)
            article['topic_scores'].append(topic.score)

        return article

    def getTitle(self, url):
        self.client.set_cleanup_return_raw(True)
        raw_text = self.client.analyze_url(url).raw_text
        soup = BeautifulSoup(raw_text, "lxml")
        return soup.title.string

    def getDate(self, url):
        # assign to each article a date. A trivial way would be to just extract the date of writing of the article. A more complicated way would be to analyze the temporal references
        # in the text to guess which one refers to the maor event. If we manage to extract a list of events referenced in the text, then maybe
        # we could do the same trick as with the keywords: let the graph decide for itself what events are related (if they are mentioned across
        # Articles for example)
        return
