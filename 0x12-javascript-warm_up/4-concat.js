#!/usr/bin/node
const process = require('process');

let arg1;
let arg2;
if (process.argv.length > 2) {
  if (process.argv.length > 3) {
    arg2 = process.argv[3];
  }
  arg1 = process.argv[2];
}
console.log(arg1 + ' is ' + arg2);
