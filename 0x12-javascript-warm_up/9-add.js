#!/usr/bin/node
function add(a, b)
{
    let result = a + b;
    console.log(result);
}
let a = parseInt(process.argv[2]);
let b = parseInt(process.argv[3]);
add(a, b);
