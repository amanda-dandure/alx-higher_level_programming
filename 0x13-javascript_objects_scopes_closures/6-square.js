#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let p = 0; p < this.height; p++) {
      let s = '';
      for (let q = 0; q < this.width; q++) {
        s += c;
      }
      console.log(s);
    }
  }
}

module.exports = Square;
