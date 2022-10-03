#!/usr/bin/node

const argNum = process.argv;

if (isNaN(Number(argNum[2]))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < argNum[2]; i++) {
    console.log('C is fun');
  }
}
