const { uri } = require('../config/configs')
const rp = require('request-promise')
const { Consulta } = require('../app/models')

module.exports.renderHome = (req, res) => {
    return res.render('home', { cep: '' })
}

module.exports.makeConsultViaCep = async (req, res) => {
    const response = await rp(uri.replace('{}', req.body.zipcode.replace(/[^0-9]/g, '')))
    const { cep, logradouro, complemento, bairro, localidade, uf, ibge, gia, ddd, siafi } = JSON.parse(response)
    console.log(Consulta);
    await Consulta.create({ cep: cep, logradouro: logradouro, complemento: complemento, bairro: bairro, localidade: localidade, uf: uf, ibge: ibge, gia: gia, ddd: ddd, siafi: siafi })
    return res.render('home', { cep, logradouro, complemento, bairro, localidade, uf, ibge, gia, ddd, siafi })
}