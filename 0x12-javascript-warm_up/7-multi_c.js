#!/usr/bin/node

let script = parseInt(process.argv[2]);

if (!isNaN(script)) {
  for (script; script > 0; script--) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of ocurrences');
}
