# NewsTime

EECE437 Team Project
Tarek Tohme, Alexandre Megarbane, Elie Tamer, Karl Hayek

A website that displays the news in timelines where events are sorted chronologically in timelines that correspond to their topic.

**Deployed app**: https://newstime437.herokuapp.com

**Dependencies**: Python3 (along with sickit-learn, matplotlib, bs4, feedparser modules), NodeJS, MongoDB.

To intialize the database with manually provided article links, run `python3 Classifier init` (do this only once because it resets the database documents).
Then, to fetch recent popular news articles at any time and add them (aggregated by timeline) to the database, run `python3 Classifier`.
Note: a local MongoDB database named newstime-dev should be created first. To use another local database or to use a remote one, edit the first line of __main__ in `Classifier/__main__.py`.

And that's the wayy the news goes.