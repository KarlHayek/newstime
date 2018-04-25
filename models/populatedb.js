//T.T. code review comments:

//Points to review:
//- include a header comment for a general description of each schema
//- include an event object that contains multiple articles (articles's ObjectId field references events instead of timelines), and events would then reference timelines. This way a user could choose among multiple news sources for an event
//- I think there's a way to automatically populate the paths of objects, check out http://mongoosejs.com/docs/populate.html
//- don't forget to include a "list of keywords" as a member in the article and timline schemas (maybe under the "array" schemaType) because that's a significant part of the output of the classifier stage
//-(for later) it would be nice to visualize the timelines as a line with clickable events on it, not as a facebook-style newsfeed
//- think of a way to search for keywords within articles and timelines, we're probably going to need that

//Good points:
//- nice idea to use mongoose, it's very flexible and it's fit for our application


const mongoose = require('mongoose');
const Schema = mongoose.Schema;

require('./Timeline');
const Timeline = mongoose.model('timelines')
require('./Article');
const Article = mongoose.model('articles')

// Map global promise - get rid of warning
mongoose.Promise = global.Promise
// Connect to mongoose
mongoose.connect('mongodb://localhost/newstime-dev')
// mongoose.connect('mongodb://karl:karl@ds129428.mlab.com:29428/newstime-prd')
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
