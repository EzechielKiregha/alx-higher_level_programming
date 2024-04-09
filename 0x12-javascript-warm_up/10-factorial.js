#!/usr/bin/node

function factorial (n) {
  return n === 0 || Number.isNaN(n) ? 1 : n * factorial(n - 1);
}

console.log(factorial(+(process.argv[2])));
