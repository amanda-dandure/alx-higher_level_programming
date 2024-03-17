#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let p = 0; p < this.height; p++) {
      let s = '';
      for (let q = 0; q < this.width; q++) {
        s += 'X';
      }
      console.log(s);
    }
  }
}

module.exports = Rectangle;
