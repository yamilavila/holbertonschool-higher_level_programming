#!/usr/bin/node

const NoArgum = process.argv[2];

if (NoArgum === undefined) {
  console.log('No argument');
} else {
  console.log(NoArgum);
}
