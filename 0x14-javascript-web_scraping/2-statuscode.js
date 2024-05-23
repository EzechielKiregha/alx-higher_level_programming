#!/usr/bin/node
// a script that displays the status code of a GET request.

const request = require('request');
const cmdArgs = process.argv.slice(2);

if (cmdArgs.length < 1) { console.log('wrong input number of arguments. provide at least one'); }

request(cmdArgs[0], (err, res) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(`code: ${res.statusCode}`);
});
