#!/usr/bin/node

const args = process.argv.slice(2);
let biggest = process.argv[2];
let i;

if (args.length > 1) {
  for (let i = 0; i < args.length; i++) {
    if (biggest < process.argv[i]) {
      biggest = process.argv[i];
    }
  }
  let secondBiggest = process.argv[3];
  for (let j = 0; j < args.length; j++) {
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
