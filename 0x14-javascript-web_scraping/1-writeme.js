#!/usr/bin/node

const filePath = process.argv[2];
const writeString = process.argv[3];
const fs = require('fs');

fs.writeFile(filePath, writeString, (err) => {
  if (err) {
    return console.error(err);
  }
});
