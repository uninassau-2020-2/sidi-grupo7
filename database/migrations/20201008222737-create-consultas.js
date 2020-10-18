'use strict';

module.exports = {
  up: (queryInterface, DataTypes) => {
    return queryInterface.createTable('Consultas', {
      id: {
        allowNull: false,
        autoIncrement: true,
        primaryKey: true,
        type: DataTypes.INTEGER,
      },
      cep: {
        allowNull: false,
        type: DataTypes.STRING,
      },
      logradouro: {
        allowNull: false,
        type: DataTypes.STRING,
        unique: true,
      },
      complemento: {
        allowNull: false,
        type: DataTypes.STRING,
      },
      bairro: {
        allowNull: false,
        type: DataTypes.STRING,
      },
      localidade: {
        allowNull: false,
        type: DataTypes.STRING,
      },
      uf: {
        allowNull: false,
        type: DataTypes.STRING,
      },
      ibge: {
        allowNull: false,
        type: DataTypes.STRING,
      },
      gia: {
        allowNull: false,
        type: DataTypes.STRING,
      },
      ddd: {
        allowNull: false,
        type: DataTypes.STRING,
      },
      siafi: {
        allowNull: false,
        type: DataTypes.STRING,
      },
      createdAt: {
        allowNull: false,
        type: DataTypes.DATE,
      },
      updatedAt: {
        allowNull: false,
        type: DataTypes.DATE,
      },
    });
  },

  down: (queryInterface) => {
    return queryInterface.dropTable('Consultas');
  }
};