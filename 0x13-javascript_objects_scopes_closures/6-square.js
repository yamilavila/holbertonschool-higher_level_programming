#!/usr/bin/node

const newSquare = require('./5-square');

module.exports = class Square extends newSquare {
  charPrint (c = 'X') {
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.height));
    }
  }
};
