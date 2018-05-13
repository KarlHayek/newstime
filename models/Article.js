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
    date_event: {
        type: Date,
        default: Date.now
    },
    topics: [{
        type: String
    }]

});

const Article = mongoose.model('articles', ArticleSchema)