require('dotenv').config({
    path: ".env.testing"
})

module.exports = {
    uri: process.env.URI,
    port: process.env.PORT
}