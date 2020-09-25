const rp = require('request-promise')
const readline = require('readline-sync')
const options = {
    uri: 'http://viacep.com.br/ws/{}/json/'
}

// CONSULTAR CEP ATRAVES DA VIACEP API
const consultCep = async (cep) => {
    options.uri = options.uri.replace('{}', cep)
    const response = await rp(options)
    return response
}

const searchCep = async () => {

    const result = readline.question(`
    CONSULTA DE CEP:
    `)
    console.log(`
    REALIZANDO CONSULTA PARA O CEP -> ${result}
    `);

    //  OBTER CEP
    const address = await consultCep(result);
    // EXIBIR CONSULTA
    console.log(JSON.parse(address));

    return searchCep()
}

searchCep()