#!/usr/bin/node

const sq = require('./5-square.js');

module.exports = class Square extends sq {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        let rect = '';
        for (let j = 0; j < this.height; j++) {
          rect += 'c';
        }
        console.log(rect);
      }
    }
  }
};
