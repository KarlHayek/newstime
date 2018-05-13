import pymongo, classifier, labler

labeler = labeler.Labeler()

# connect to local database
db = MongoClient('mongodb://localhost:27017')['newstime-dev']
# connect to production database
# db = MongoClient('mongodb://ds129428.mlab.com:29428/')['newstime-prd']
# db.authenticate('karl', 'karl') # username and passw

articles = db.waitlist.find()

# perform clustering on the articles, using hierarchical clustering with single linkage,
# and using as distanceds the inverse of the simliarity scores obtained from calling
# classifier.getSimilarityScore() on all the pairs of articles

import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

samples = [
    [0, 1, 2, 3],
    [1, 0, 4, 0.5],
    [2, 4, 0, 1.5],
    [3, 0.5, 1.5, 0],
]

# Calculate the linkage: mergings
mergings = linkage(samples)

# Plot the dendrogram
dendrogram(mergings,
           #            labels=article_names,
           leaf_rotation=90,
           leaf_font_size=6,
           )
plt.show()



# go over all the clusters. For every good cluster, add it to the timeline.
# Use the first three labels of this timline as an arbitrary title for the timeline
