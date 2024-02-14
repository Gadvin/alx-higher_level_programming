#!/usr/bin/node
const process = require('process');

function factorialize (number)
{
  if (isNaN(number))
  {
    return 1;
  }
  if (number < 0)
  {
    return -1;
  }
  else if (number === 0)
  {
    return 1;
  }
  else
  {
    return (number * factorialize(number - 1));
  }
}

console.log(factorialize(parseInt(process.argv[2])));
