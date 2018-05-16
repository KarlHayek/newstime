if (process.env.NODE_ENV === 'production'){
    // connect to online database
    module.exports = { mongoURI: 'mongodb://karl:karl@ds129428.mlab.com:29428/newstime-prd'}
} else {
    // connect to local database
    module.exports = { mongoURI: 'mongodb://localhost/newstime-dev'}
}