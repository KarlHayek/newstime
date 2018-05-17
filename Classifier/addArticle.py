import classifier

def addArticle(article, db):
    # add the article to the articles collection
    article_id = db.insertArticle(article)

    # print("Now dealing with", article['title'], "...")
    foundAtLeastOneTimeline = False
    similarities = []
    for timeline in db.timelines.find():
        # compare the article's topics to timeline's topics
        similarity = classifier.getSimilarityScore(article['topics'], timeline['topics'])
        similarities.append(similarity)

        print("similarities per timeline:", similarities)
        # if the correlation is high enough, add the article to the timeline
        if similarity > 0.34:   # magic number
            print("ADDED", article['title'], ' TO TIMELINE ', timeline['title'])
            timeline['articles'].append(article_id)
            # update the timeline's topics from all of its articles
            timeline['topics'] = classifier.getTimelineTopicsFromArticles(db.getArticlesFromTimeline(timeline))

            db.updateTimeline(timeline)
            foundAtLeastOneTimeline = True
    
    # add the article to the waitlist if it wasn't added to any timeline
    if foundAtLeastOneTimeline == False:
        article['waitlisted'] = True
        article['waitlist_TTL'] = 5
        db.updateArticle(article)
        print("WAITLISTED ARTICLE", article['title'])
        return 1
    
    return 0