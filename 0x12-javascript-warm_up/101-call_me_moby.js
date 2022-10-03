#!/usr/bin/node

exports.callMeMoby = function (x, myFunc) {
  for (let i = 0; i < x; i++) {
    myFunc();
  }
};
