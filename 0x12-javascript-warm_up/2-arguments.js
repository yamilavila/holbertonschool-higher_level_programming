#!/usr/bin/node

const argum = process.argv;

if (argum.length === 2) {
  console.log('No argument');
} else if (argum.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
