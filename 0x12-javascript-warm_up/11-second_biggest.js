#!/usr/bin/node

const args = process.argv;
let biggest = process.argv[2];
const firstArg = process.argv[0];
const secondArg = process.argv[1];

let i;

if (!(firstArg && secondArg && (args.length < 4))) {
  for (let i = 2; i < args.length; i++) {
    if (biggest < process.argv[i]) {
      biggest = process.argv[i];
    }
  }
  let secondBiggest = process.argv[2];
  for (let j = 2; j < args.length; j++) {
    if (process.argv[j] !== biggest && i !== j) {
      if (process.argv[j] > secondBiggest) {
        secondBiggest = process.argv[j];
      }
    }
  }
  console.log(secondBiggest);
} else {
  console.log(0);
}
