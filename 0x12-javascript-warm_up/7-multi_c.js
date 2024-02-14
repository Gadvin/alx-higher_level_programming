#!/usr/bin/node
const process = require('process');
let build = '';
let error_msg = 'Missing number of occurrences';
let number;
let i;

if (process.argv.length > 2) {
  number = parseInt(process.argv[2]);
  if (isNaN(number)) {
    build = error_msg;
  } else {
    for (i = 0; i < number; i++) {
      if (i > 0) {
        build += '\n';
      }
      build += 'C is fun';
    }
  }
} else {
  build = error_msg;
}
if (build !== '') {
  console.log(build);
}
