const port  = 8081
const express = require('express')
const app = express()
const bodyParser = require('body-parser')
const { makeConsultViaCep, renderHome } = require('./routes')


app.use(bodyParser.urlencoded({ extended: true }))
app.use(bodyParser.json())
app.set('view engine', 'ejs')

app.get('/', (req, res) => {
    res.send(`<strong>EM DESENVOLVIMENTO</strong>`)
})

app.get('/zipcode', renderHome)

app.post('/zipcode', makeConsultViaCep)

app.get('*', (req, res) => {
    res.redirect('/')
})

app.listen(port, () => {
    console.log(`The server is running on http://localhost:${port}`)
})