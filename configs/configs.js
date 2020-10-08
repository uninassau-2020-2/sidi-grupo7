require('dotenv').config({
    path: process.env.NODE_ENV === "dev" ? ".env.testing" : ".env"
})

module.exports = {
    uri: 'http://viacep.com.br/ws/{}/json/',
    port: process.env.PORT
}