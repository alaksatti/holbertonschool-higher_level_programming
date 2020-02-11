#!/usr/bin/node
// class square
const oldsquare = require('./5-square');

class Square extends oldsquare {
  constructor (size) { super(size, size); }

  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) { console.log(c.repeat(this.width)); }
  }
}
module.exports = Square;
