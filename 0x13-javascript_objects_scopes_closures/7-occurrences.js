#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach(value => {
    if (value === searchElement) {
      count++;
    }
  });
  return count;
};
