#!/usr/bin/node

const myArgs = process.argv.slice(2);
const fs = require('fs');

fs.writeFile(myArgs[0], myArgs[1], (err) => {
  if (err) throw err;
});
