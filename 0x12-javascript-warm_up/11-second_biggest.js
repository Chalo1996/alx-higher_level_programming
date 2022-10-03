#!/usr/bin/node

const argsLen = process.argv.length;
let biggest = process.argv[2];
let i;

if (argsLen <= 3) {
  console.log(0);
} else {
  for (let i = 0; i < argsLen; i++) {
    if (biggest < process.argv[i]) {
      biggest = process.argv[i];
    }
  }
  let secondBiggest = process.argv[3];
  for (let j = 0; j < argsLen; j++) {
    if (process.argv[j] !== biggest && i !== j) {
      if (process.argv[j] > secondBiggest) {
        secondBiggest = process.argv[j];
      }
    }
  }
  console.log(secondBiggest);
}
