const express = require('express')
const os = require('os')

const { exit } = require('process')
const mysql = require('mysql2');
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'Sathvik22',
  database: 'gamedb'
});


const app = express()
const port = 3000

const netint = os.networkInterfaces()
if(!netint["Wi-Fi"])
{
    console.log("Wi-Fi is not connected,exiting..");
    exit(1)
}
const ip = netint["Wi-Fi"].slice(-1)[0].address

let loggedIn=false

app.get('/', (req, res) => {
  res.sendFile(__dirname + "/index.html")
})

app.get('/data', (req, res) => {
  
  if (!loggedIn){
    return res.send("not logged in !")

  }
  connection.query('SELECT * FROM profiles', (error, results, fields) => {
    if (error) {
      console.error('Error executing query:', error);
      return;
    }
    console.log(fields)
    res.send('Query results:'+ JSON.stringify(results));
  });
  

  // res.sendFile(__dirname + "/Game.sql")
})
app.get('/logout', (req, res) => {
  

  loggedIn=false
  res.send("logout success !")

  // connection.end((err) => {
  //   if (err) {
  //     console.error('Error closing the connection:', err);
  //   }else{

   
  //   }
  // });
  

})
app.get('/login', (req, res) => {
  
  loggedIn=true
  res.send("login success !")

})


app.listen(port )
console.log(` server up and running, listening at http://127.0.0.1:${port}/`);








