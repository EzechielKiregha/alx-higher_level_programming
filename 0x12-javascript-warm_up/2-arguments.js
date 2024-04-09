#!/usr/bin/node

const arg_count = process.argv.length;
console.log(arg_count === 2 ? 'No argument' : arg_count === 3 ? 'Argument found' : 'Arguments found');
