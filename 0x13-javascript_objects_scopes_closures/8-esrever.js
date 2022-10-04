#!/usr/bin/node

exports.esrever = function (list) {
  const revList = [];
  for (let j = 0; j < list.length; j++) {
    revList.unshift(list[j]);
  }
  return revList;
};
