#!/usr/bin/node

const sq = require('./5-square.js');

module.exports = class Square extends sq {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let rect = '';
        for (let j = 0; j < this.width; j++) {
          rect += 'C';
        }
        console.log(rect);
      }
    }
  }
};
