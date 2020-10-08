const { uri } = require('../configs/configs')
const rp = require('request-promise')

module.exports.renderHome = (req, res) => {
    return res.render('home', { cep: '' })
}

module.exports.makeConsultViaCep = async (req, res) => {
    const response = await rp(uri.replace('{}', req.body.zipcode.replace(/[^0-9]/g, '')))
    const { cep, logradouro, complemento, bairro, localidade, uf, ibge, gia, ddd, siafi } = JSON.parse(response)
    return res.render('home', { cep, logradouro, complemento, bairro, localidade, uf, ibge, gia, ddd, siafi })
}