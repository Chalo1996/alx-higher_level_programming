#!/usr/bin/node

// const args = process.argv;
// let biggest = process.argv[2];
// const firstArg = process.argv[0];
// const secondArg = process.argv[1];
// let i;

// if (args.length > 1 && args !== firstArg && args !== secondArg) {
//   for (let i = 0; i < args.length; i++) {
//     if (biggest < process.argv[i]) {
//       biggest = process.argv[i];
//     }
//   }
//   let secondBiggest = process.argv[3];
//   for (let j = 0; j < args.length; j++) {
//     if (process.argv[j] !== biggest && i !== j) {
//       if (process.argv[j] > secondBiggest) {
//         secondBiggest = process.argv[j];
//       }
//     }
//   }
//   console.log(secondBiggest);
// } else {
//   console.log(0);
// }

let secondLargest = 0;
const args = process.argv.slice(2);

if (args.length > 1) {
  args.sort();
  secondLargest = args[args.length - 2];
}
console.log(secondLargest);
