const mongoose = require('mongoose');
const Schema = mongoose.Schema;

// DB Config
const db = require('../config/database');

require('./Timeline');
const Timeline = mongoose.model('timelines')
require('./Article');
const Article = mongoose.model('articles')

// Map global promise - get rid of warning
mongoose.Promise = global.Promise
// Connect to mongoose
mongoose.connect(db.mongoURI)
    .then(() => console.log('MongoDB Connected...'))
    .catch(err => console.log(err));


var timelineArticles = [[
    {
        title: "Donald Trump's Wall is getting push back from Congress ",
        link: "https://www.washingtontimes.com/news/2018/apr/12/donald-trumps-wall-is-getting-push-back-from-congr/",
        _id: mongoose.Types.ObjectId()
    },
    {
        title: "Donald Trump is up to his usual shenanigans ",
        link: "https://www.somewebsite.com",
        _id: mongoose.Types.ObjectId()
    }
    ],
    [{
        title: "The privacy question Mark Zuckerberg kept dodging",
        link: "https://www.vox.com/policy-and-politics/2018/4/11/17225518/mark-zuckerberg-testimony-facebook-privacy-settings-sharing",
        _id: mongoose.Types.ObjectId()
    }]
]

timelineArticles.forEach((articles) => {
    articles.forEach(article => {
        new Article(article)
            .save()
    })
})

var newTimelines = [
    {
        title: "Trump Wall",
        details: "Events related to the wall that President Trump wants to erect in the US-Mexico border",
        articles: []
    },
    {
        title: "The Zucc",
        details: "The adventures Marc Zuckerberg",
        articles: []
    }
]

var index = 0;
newTimelines.forEach(timeline => {
    timelineArticles[index].forEach(article => {
        timeline.articles.push(article._id)
    })
    index++;
})

newTimelines.forEach(timeline => {
    new Timeline(timeline)
        .save()
})
