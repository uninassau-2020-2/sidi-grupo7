require('dotenv').config({
  path: ".env.testing"
})

module.exports = {
  username: 'root',
  password: process.env.DATABASE_PASS,
  database: process.env.DATABASE,
  host: process.env.DATABASE_CONNECTION,
  port: process.env.DATABASE_PORT,
  dialect: 'mysql'
}