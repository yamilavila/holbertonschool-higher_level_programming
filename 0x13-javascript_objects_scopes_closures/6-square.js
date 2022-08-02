#!/usr/bin/node

class Square extends require('./5-square') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    for (let i = this.height; i--;) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
