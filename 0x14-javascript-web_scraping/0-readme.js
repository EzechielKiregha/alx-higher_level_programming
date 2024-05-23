#!/usr/bin/node
// a script that reads and prints the content of a file.

const fs = require('fs');

const cmdArgs = process.argv.slice(2);

const readFileAsync = (filePath, encoding) => {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, encoding, (err, data) => {
      if (err) {
        reject(err);
      } else {
        resolve(data);
      }
    });
  });
};

(async () => {
  try {
    const data = await readFileAsync(cmdArgs[0], 'utf8');
    console.log(data);
  } catch (err) {
    console.error(err);
  }
})();
