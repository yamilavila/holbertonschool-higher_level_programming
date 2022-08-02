#!/usr/bin/node

if (process.argv.length > 3) {
  const seconBigNum = process.argv.sort(function (a, b) { return b - a; });
  console.log(seconBigNum[3]);
} else {
  console.log(0);
}
