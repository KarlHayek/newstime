from pymongo import MongoClient
import classifier, matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster


# connect to local database
db = MongoClient('mongodb://localhost:27017')['newstime-dev']
# connect to production database
# db = MongoClient('mongodb://ds129428.mlab.com:29428/')['newstime-prd']
# db.authenticate('karl', 'karl') # username and passw

articles = []
articleTopics, articleTitles = [], []
waitlist = db.articles.find({'waitlisted': True})

for article in waitlist:
    articleTopics.append(article['topics'])
    articleTitles.append(article['title'])
    articles.append(article)

articleIndexes = [i for i in range(len(articleTitles))]

# condensed 1-d matrix representing the distances between all articles
# it is of size (n choose 2) where n is the number of articles
distances = []
condensedNames = []  # for testing

m = len(articleTopics)
for i in range(0, m - 1):
    for j in range(i + 1, m):
        distances.append(
            1/classifier.getSimilarityScore(articleTopics[i], articleTopics[j]))
        condensedNames.append(articleTitles[i] + " | WITH | " + articleTitles[j]) # for testing

# Calculate the linkage (hierarchical clustering)
mergings = linkage(distances, method='average')

## for testing:
## for i in range(len(distances)):
##     print(condensedNames[i], ":", distances[i])
# for i in range(len(articleTitles)):
#     print(articleIndexes[i], ":", articleTitles[i])
# dendrogram(mergings, labels=articleIndexes)
# plt.show()



# height is how 'good' we want our clusters to be
height = 8
# get labels from the different obtained clusters
labels = fcluster(mergings, height, criterion='distance')

# make a dict of cluster labels that point to article indices
articlesPerLabels = dict((x, []) for x in labels)
for i, label in enumerate(labels):
    articlesPerLabels[label].append(i)


for articleIndices in articlesPerLabels.values():
    # if there are 3+ articles in the cluster, add it as a timeline to the timelines collection
    if len(articleIndices) < 3: continue
    
    # get the full articles from their indices
    arts = [articles[index] for index in articleIndices]

    topics = classifier.getTimelineTopicsFromArticles(arts)
    timeline = {
        'title': ' '.join(topics[:4]),
        'details': ' '.join(topics[:8]),
        'articles': [art['_id'] for art in arts],
        'topics': topics,
    }

    db.timelines.insert_one(timeline)
    print("Added timeline", timeline['title'], "from", len(articleIndices), "articles")
#     print(timeline)

    # remove the articles from the waitlist
    for art in arts:
        art['waitlisted'] = False
        db.articles.update_one({'_id': art['_id']}, {"$set": art}, upsert=False)