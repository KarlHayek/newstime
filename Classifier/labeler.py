# The labeler takes a url of a news article, extracts topics from the text and writes them in a text file.

import textrazor, pprint, datetime
from bs4 import BeautifulSoup

textrazor.api_key = "5634740d9e8d89a14374edaa305c207bd6eda5918bbe233634beb092"

class Labeler:
    def __init__(self):
        self.client = textrazor.TextRazor(extractors=["topics"])  # instance of TextRazor class

    def extractIntoArticle(self, url):
        self.client.set_cleanup_return_raw(True)    # for getting the title
        self.response = self.client.analyze_url(url)

        article = {
            'link': url,
            'title': self.getTitle(),
            'topics':[],
            'topic_scores': [],
            'waitlisted': False,
            'date_added': datetime.datetime.utcnow()
        }


        for topic in self.response.topics():
            if topic.score < 0.4:   # magic number
                break   # don't add low-score topics
            article['topics'].append(topic.label)
            article['topic_scores'].append(topic.score)

        return article

    def getTitle(self):
        raw_text = self.response.raw_text
        soup = BeautifulSoup(raw_text, "lxml")
        return soup.title.string

