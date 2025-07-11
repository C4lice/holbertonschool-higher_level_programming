#!/usr/bin/node

const { argv } = require('node:process');

if (isNaN(argv[3])) {
  console.log(0);
} else {
  let biggest = argv[2];
  let secBiggest = argv[3];
  let value;
  argv.forEach(function (val, index, argv) {
    value = parseInt(val);
    if (value > biggest) {
      secBiggest = biggest;
      biggest = value;
    } else if (value < biggest && value > secBiggest) {
      secBiggest = value;
    }
  });
  console.log(secBiggest);
}
