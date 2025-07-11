#!/usr/bin/node

const { argv } = require('node:process');

const theFirstNumber = argv[2];
const theSeconNumber = argv[3];

function add (theFirstNumber, theSeconNumber) {
  theFirstNumber = parseInt(theFirstNumber);
  theSeconNumber = parseInt(theSeconNumber);
  if (isNaN(theFirstNumber) || isNaN(theSeconNumber)) {
    console.log(NaN);
  } else {
    console.log(theFirstNumber + theSeconNumber);
  }
}

add(theFirstNumber, theSeconNumber);
