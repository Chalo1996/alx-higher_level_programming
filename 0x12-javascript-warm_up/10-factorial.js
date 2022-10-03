#!/usr/bin/node

const firstInt = process.argv[2];

function fact (x) {
  if (isNaN(x)) {
    return (1);
  } else {
    if (x === 1) {
      return (1);
    } else {
      return (x * fact(x - 1));
    }
  }
}

console.log(fact(firstInt));
