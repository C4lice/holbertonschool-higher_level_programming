#!/usr/bin/node

const { argv } = require('node:process');

let count = 0;
let theNumber;

argv.forEach(function (val, index, argv) {
  count += 1;
  if (count === 3) {
    theNumber = val;
  }
});

theNumber = parseInt(theNumber);
if (isNaN(theNumber)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + theNumber);
}
