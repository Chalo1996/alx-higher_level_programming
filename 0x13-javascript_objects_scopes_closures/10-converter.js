#!/usr/bin/node

exports.converter = function (base) {
  function converterNum (num) {
    return num.toString(base);
  }
  return converterNum;
};
