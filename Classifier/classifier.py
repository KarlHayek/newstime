import classifier, matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from collections import OrderedDict


def getSimilarityScore(topics1, topics2, topic_scores1=[], topic_scores2=[]):
    topicsWeight = 0.1
    
    if len(topics1) == 0 or len(topics2) == 0:
        print("Error: one of the passed topics arrays is empty!")
        return

    score = 0
    for topic1 in topics1:
        for topic2 in topics2:
            if(topic1 == topic2):
                score += topicsWeight   # multiply by topic confidence score

    score = score / (len(topics1) * (topicsWeight))       # normalize the scores
    return score



def getTimelineTopicsFromArticles(articles):
    keywordRelevance = {}; size = 0

    for article in articles:
        for i in range(len(article['topics'])):
            # if the keyword hasn't been entered yet
            if (not article['topics'][i] in keywordRelevance):
                keywordRelevance[article['topics'][i]] = 0
            else:
                # increment frequency for 'keyword' 
                keywordRelevance[article['topics'][i]] += article['topic_scores'][i]
        size+=1

    # order by score
    ordered = OrderedDict(sorted(keywordRelevance.items(), key=lambda t: t[1], reverse=True))
    timelineTopics = []
    for keyword, relevance in ordered.items():
        if relevance > 0.2 * size:      # if the keyword appears in more than a certain fraction of the number of articles
            timelineTopics.append(keyword)

    return timelineTopics


def handleWaitlistArticles(waitlist):
    articles = [article for article in waitlist]
    articleTopics = [art['topics'] for art in articles]
    articleTitles = [art['title'] for art in articles]
    articleIndices = [i for i in range(len(articleTitles))]
    addedTimelines, addedArticles = [], []
    
    # condensed 1-d matrix of size (n choose 2) representing the distances between all articles
    distances, comparisonNames = [], []

    m = len(articleTopics)
    for i in range(0, m - 1):
        for j in range(i + 1, m):
            distances.append(1 / classifier.getSimilarityScore(articleTopics[i], articleTopics[j]))
            comparisonNames.append(articleTitles[i] + " | WITH | " + articleTitles[j])  # for testing

    # Calculate the linkage (hierarchical clustering)
    mergings = linkage(distances, method='average')

    ## for testing:
    ## for i in range(len(distances)):
    ##     print(comparisonNames[i], ":", distances[i])
    # for i in range(len(articleTitles)):
    #     print(articleIndices[i], ":", articleTitles[i])
    # dendrogram(mergings, labels=articleIndices)
    # plt.show()


    # height is how 'good' we want our clusters to be
    height = 8
    # get labels from the different obtained clusters
    labels = fcluster(mergings, height, criterion='distance')

    # make a dict of cluster labels that represent article indices
    articlesPerLabels = dict((x, []) for x in labels)
    for i, label in enumerate(labels):
        articlesPerLabels[label].append(i)


    for articleIndices in articlesPerLabels.values():
        # if there are 3+ articles in the cluster, add it as a timeline to the timelines collection
        if len(articleIndices) < 3:
            continue

        # get the full articles from their indices
        arts = [articles[index] for index in articleIndices]
        topics = classifier.getTimelineTopicsFromArticles(arts)

        timeline = {
            'title': ' '.join(topics[:4]),
            'details': ' '.join(topics[:8]),
            'articles': [art['_id'] for art in arts],
            'topics': topics,
        }

        addedTimelines.append(timeline)
        print("Added timeline", timeline['title'], "from", len(articleIndices), "articles")

        # remove the added articles from the waitlist
        for art in arts:
            art['waitlisted'] = False
            addedArticles.append(art)
    
    return addedTimelines, addedArticles
