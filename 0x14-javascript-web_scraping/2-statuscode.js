#!/usr/bin/node

const myArgs = process.argv.slice(2);
const req = require('request');

req(myArgs[0], (err, res, req) => {
  if (err) throw err;

  const status = res && res.statusCode;
  console.log(`code: ${status}`);
});
