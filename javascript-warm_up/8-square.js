#!/usr/bin/node

const { argv } = require('node:process');
let col = 0;
let row = 0;
let rowstring = '';

if (isNaN(argv[2])) {
  console.log('Missing size');
}

while (col < argv[2]) {
  while (row < argv[2]) {
    rowstring += 'X';
    row++;
  }
  console.log(rowstring);
  rowstring = '';
  row = 0;
  col++;
}
