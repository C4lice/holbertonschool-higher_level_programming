#!/usr/bin/node

const { argv } = require('node:process');

let count = 0;
let firstWord;
let secondWord;

argv.forEach(function (val, index, argv) {
  count += 1;
  if (count === 3) {
    firstWord = val;
  } else if (count === 4) {
    secondWord = val;
  }
});

console.log(firstWord + ' is ' + secondWord);
