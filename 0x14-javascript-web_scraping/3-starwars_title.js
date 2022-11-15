#!/usr/bin/node

const myArgs = process.argv.slice(2);
const res = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';

res(url + myArgs[0], (err, res, body) => {
  if (err) throw err;

  console.log(JSON.parse(body).title);
});
