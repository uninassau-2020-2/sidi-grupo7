module.exports = (sequelize, DataTypes) => {
    const Consulta = sequelize.define('Consulta', {
        cep: DataTypes.STRING,
        logradouro: DataTypes.STRING,
        complemento: DataTypes.STRING,
        bairro: DataTypes.STRING,
        localidade: DataTypes.STRING,
        uf: DataTypes.STRING,
        unidade: DataTypes.STRING,
        ibge: DataTypes.STRING,
        gia: DataTypes.STRING,
        ddd: DataTypes.STRING,
        siafi: DataTypes.STRING
    }, {
        tableName: 'Consultas'
    });

    return Consulta;
}