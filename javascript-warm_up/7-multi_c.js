#!/usr/bin/node

const { argv } = require('node:process');
let count = 0;

if (isNaN(argv[2])) {
  console.log('Missing number of occurrences');
}

while (count < argv[2]) {
  console.log('C is fun');
  count++;
}
