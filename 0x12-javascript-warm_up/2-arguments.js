#!/usr/bin/node

const argNum = process.argv.length;

switch (argNum) {
  case 2:
    console.log('No argument');
    break;

  case 3:
    console.log('Argument found');
    break;

  default:
    console.log('Arguments found');
}
