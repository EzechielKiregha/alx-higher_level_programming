#!/usr/bin/node

// modules
const fs = require('fs').promises;
const { argv } = require('process');

fs.readFile(argv[2], 'utf8')
  .then(data => fs.writeFile(argv[4], data, 'utf8'))
  .catch(e => console.error(e));

fs.readFile(argv[3], 'utf8')
  .then(data => fs.writeFile(argv[4], data, { flag: 'a' }, 'utf8'))
  .catch(e => console.error(e));
