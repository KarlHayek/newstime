const mongoose = require('mongoose');
const Schema = mongoose.Schema;

// Create Schema
const TimelineSchema = new Schema({
    title: {
        type: String,
        required: true
    },
    details: {
        type: String
    },
    articles: [{
        type: Schema.Types.ObjectId, ref: 'articles'
    }],
    date: {
        type: Date,
        default: Date.now
    },
    topics: [{
        type: String
    }],
    topic_scores: [{
        type: Number
    }]
});

const Timeline = mongoose.model('timelines', TimelineSchema)