#!/usr/bin/node

'use strict';

let argNum = process.argv[2];

if (isNaN(argNum)) {
  console.log('Not a number');
} else {
  console.log('My number is: '+argNum);
}
