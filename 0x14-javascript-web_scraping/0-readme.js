#!/usr/bin/node

const myArg = process.argv.slice(2);
const fs = require('fs');

fs.readFile(myArg[0], (err, data) => {
  if (err) throw err;

  console.log(data.toString());
});
