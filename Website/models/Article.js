const mongoose = require('mongoose');
const Schema = mongoose.Schema;

// Create Schema
const ArticleSchema = new Schema({
    title: {
        type: String,
        required: true
    },
    link: {
        type: String,
        required: true
    },
    // stories: [{
    //     type: Schema.Types.ObjectId, ref: 'Story'
    // }],
    date_added: {
        type: Date,
        // default: Date.now
    },
    topics: [{
        type: String
    }],
    topic_scores: [{
        type: Number
    }],
    waitlisted: {
        type: Boolean
    },
    waitlist_TTL :{
        type: Number,
        default: 5
    }
});

const Article = mongoose.model('articles', ArticleSchema)