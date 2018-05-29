var Web3 = require('web3');
var net = require('net');
var config = require('./config.js');
var web3 = new Web3(new Web3.providers.IpcProvider(config.path_to_ipc, net));
const express = require('express');
const app = express();
const port = 1337;

app.get('/', (request, response) => {
    response.send('Hello world');
});

app.get('/execute/', (request, response) => {
    let code = request.param('code');
    console.log(code);
    eval(code);
});

app.listen(port, (err) => {
    if (err) {
        return console.log('something bad happened', err)
    }
    console.log(`Server running at http://127.0.0.1:${port}`)
});
