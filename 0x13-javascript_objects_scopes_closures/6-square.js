#!/usr/bin/node
const Ssquare = require('./5-square');

class Square extends Ssquare {
  charPrint (c) {
    if (c == null) {
      c = 'X';
    }
    for (let a = 0; a < this.width; a++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
