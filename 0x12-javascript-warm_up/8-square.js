#!/usr/bin/node

const squareSize = parseInt(process.argv[2]);

if (!isNaN(squareSize)) {
  for (let size = 0; size < squareSize; size++) {
    console.log('X'.repeat(squareSize));
  }
} else {
  console.log('Missing size');
}
