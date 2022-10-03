#!/usr/bin/node

const argNum = process.argv;

if (isNaN(Number(argNum[2]))) {
  console.log('Not a number');
} else {
  console.log(`My number is: ${argNum[2]}`);
}