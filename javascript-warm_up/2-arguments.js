#!/usr/bin/node

const { argv } = require('node:process');

const firstv = 'No argument';
const seconv = 'Argument found';
const thirdv = 'Arguments found';

let count = 0;

argv.forEach(function (val, index, argv) {
  count += 1;
});

if (count === 2) {
  console.log(firstv);
} else if (count === 3) {
  console.log(seconv);
} else {
  console.log(thirdv);
}
