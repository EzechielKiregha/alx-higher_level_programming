#!/usr/bin/node
// a script that computes the number of tasks completed by user id.

const request = require('request');
const cmdArgs = process.argv.slice(2);
const usersObj = {};

if (cmdArgs.length < 1) {
  console.log('wrong number of input arguments. requires at least 1');
  process.exit(98);
}

const requestUrl = cmdArgs[0];

const fetchEndpoint = async () => {
  return new Promise((resolve, reject) => {
    request(requestUrl, (err, res) => {
      if (err) {
        reject(err);
      }
      const body = JSON.parse(res.body);
      resolve(body);
    });
  });
};

(async () => {
  const response = await fetchEndpoint();
  for (const todo of response) {
    if (todo.completed) {
      if (!(todo.userId in usersObj)) {
        usersObj[todo.userId] = 1;
      } else {
        usersObj[todo.userId] = usersObj[todo.userId] + 1;
      }
    }
  }
  console.log(usersObj);
})();
