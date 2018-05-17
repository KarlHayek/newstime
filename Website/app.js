const express = require('express');
const exphbs = require('express-handlebars')
const mongoose = require('mongoose')

const app = express();  // init application

// DB Config
const db = require('./config/database');

// Map global promise - get rid of warning
mongoose.Promise = global.Promise
// Connect to mongoose
mongoose.connect(db.mongoURI)
    .then(() => console.log('MongoDB Connected...'))
    .catch(err => console.log(err));


// Load Timeline Model
require('./models/Timeline');
const Timeline = mongoose.model('timelines')
require('./models/Article');
const Article = mongoose.model('articles')

// Handlebars middleware
app.engine('handlebars', exphbs({
    defaultLayout: 'main'
}));

app.set('view engine', 'handlebars')

app.use(express.static(__dirname)); // for including the css file

// Index Route
app.get('/', (req, res) => {
    res.render('index');
});

// Timeline Index Page
app.get('/timelines', (req, res) => {
    var query = {};
    var searchResponse = "";
    if (req.query.search) {
        // case insensitive title and topic search
        query = {$or: [
                {title: new RegExp(req.query.search, "i")},
                {topics: new RegExp(req.query.search, "i")}
            ]}
    }
    Timeline.find(query)
        .sort({date: 'desc'})
        .then(timelines => {
            if (req.query.search) {
                searchResponse = `Found ${timelines.length} search results for '${req.query.search}':`;
            }
            timelines.forEach(timeline => { timeline.topics = timeline.topics.slice(0,8) })
            res.render('timelines/index', {
                timelines: timelines,
                searchResponse: searchResponse
            });
        })
})



// Show Timeline Route
app.get('/timelines/show/:id', (req, res) => {
    Timeline.findOne({
        _id: req.params.id
    })
        .populate('articles')
        .then(timeline => {
            res.render('timelines/show', {
                timeline: timeline
            });
        })
})

const port = process.env.PORT || 5000;

app.listen(port, () => {
    console.log('Server started on port ' + port);
})
