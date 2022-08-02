#!/usr/bin/node

exports.esrever = function (list) {
  const backwardList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    backwardList.push(list[i]);
  }
  return backwardList;
};
