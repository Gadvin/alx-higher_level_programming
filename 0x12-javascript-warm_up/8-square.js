#!/usr/bin/node
const process = require('process');
let build = '';
let error_msg = 'Missing size';
let number;
let i;
let j;

if (process.argv.length > 2) {
  number = parseInt(process.argv[2]);
  if (isNaN(number)) {
    build = error_msg;
  } else {
    for (i = 0; i < number; i++) {
      if (i > 0) {
        build += '\n';
      }
      for (j = 0; j < number; j++) {
        build += 'X';
      }
    }
  }
} else {
  build = error_msg;
}
if (build !== '') {
  console.log(build);
}
