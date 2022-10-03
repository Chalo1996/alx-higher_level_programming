#!/usr/bin/node

const argNum = process.argv;

if (argNum[2]) {
  console.log(argNum[2]);
} else {
  console.log('No argument');
}
