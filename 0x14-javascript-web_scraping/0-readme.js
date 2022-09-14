#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];

fs.readFile(file, 'utf8', error);

function error (bad, data) {
  if (bad) {
   console.log(bad);
  } else {
    process.stdout.write(data);
  }
}
