#!/usr/bin/node

let string = 0;

exports.logMe = function (item) {
  console.log(string + ': ' + item);
  string++;
};
