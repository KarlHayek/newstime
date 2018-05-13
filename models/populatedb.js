////// !! This file is not used anymore. Instead a python file that does
////// !! the same thing and gets the article and tmieline topics was written

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



var timelineArticles = [
    [
        {
            title: "Donald Trump's Wall is getting push back from Congress ",
            link: "https://www.washingtontimes.com/news/2018/apr/12/donald-trumps-wall-is-getting-push-back-from-congr/"
        },
        {
            title: "Donald Trump is up to his usual shenanigans ",
            link: "https://www.somewebsite.com"
        }
    ],
    [
        {
            title: "The privacy question Mark Zuckerberg kept dodging",
            link: "https://www.vox.com/policy-and-politics/2018/4/11/17225518/mark-zuckerberg-testimony-facebook-privacy-settings-sharing"
        }
    ]
]

var newTimelines = [
    {
        title: "Trump Wall",
        details: "Events related to the wall that President Trump wants to erect in the US-Mexico border"
    },
    {
        title: "The Zucc",
        details: "The adventures Marc Zuckerberg"
    }
]


var index = 0;
newTimelines.forEach(timeline => {
    timeline["articles"] = []

    // go over the timeline's articles
    timelineArticles[index].forEach(article => {
        // save the article
        article["_id"] = mongoose.Types.ObjectId(); article["topics"] = []
        new Article(article).save()

        // fill the article's id in its timeline
        timeline["articles"].push(article._id)
    })

    new Timeline(timeline).save()
    index++;
})