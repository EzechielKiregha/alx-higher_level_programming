#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const arguments = process.argv.map(el=>+el)
    .slice(2, process.argv.length)
    .sort((a, b) => a - b);
  console.log(arguments[arguments.length - 2]);
}
