#!/usr/bin/node

const num_arg = Math.trunc(Number(process.argv[2]));
console.log(isNaN(num_arg) ? 'Not a number' : `My number: ${num_arg}`);
