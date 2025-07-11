#!/usr/bin/node

const { argv } = require('node:process');

const firstv = 'No argument';
let count = 0;

argv.forEach(function (val, index, argv) {
  count += 1;
  if (count === 3) {
    console.log(val);
  }
});

if (count === 2) {
  console.log(firstv);
}
