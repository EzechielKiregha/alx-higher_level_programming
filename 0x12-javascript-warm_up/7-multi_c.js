#!/usr/bin/node

const times = Math.trunc(Number(process.argv[2]));
if (Number.isNaN(times)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < times; i++) {
    console.log('C is fun');
  }
}
