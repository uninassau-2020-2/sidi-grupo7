require('dotenv').config({
    path: process.env.NODE_ENV === "test" ? ".env.testing" : ".env"
})

module.exports = {
    uri: process.env.URI
}