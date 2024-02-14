#!/usr/bin/node
const process = require('process');
let message = 'Not a number';
let number;

if (process.argv.length > 2) {
  number = parseInt(process.argv[2]);
  if (!isNaN(number)) {
    message = 'My number: ' + String(number);
  }
}
console.log(message);
