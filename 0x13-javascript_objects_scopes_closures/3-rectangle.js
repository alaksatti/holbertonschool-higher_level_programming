#!/usr/bin/node
// create an empty class rectangle '
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || isNaN(w) || h <= 0 || isNaN(h)) { return this; }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) { console.log('X'.repeat(this.width)); }
  }
}
module.exports = Rectangle;
