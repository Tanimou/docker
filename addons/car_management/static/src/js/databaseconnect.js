//npm install pg
const { Client } = require('pg');

const client = new Client({
    host: 'localhost',
    user: 'postgres',
    password: 'Candycove456',
    database: 'postgres',
    port: 5432,

})

client.connect()
client.query('SELECT * FROM actor', (err, res) => {
    if(err){
        console.log(err.stack)
    }else{
        console.log(res.rows)
    }
    client.end
 })