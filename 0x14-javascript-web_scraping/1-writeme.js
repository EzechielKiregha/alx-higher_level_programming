#!/usr/bin/node
// a script that writes a content to a file.

const fs = require('fs');

const cmdArgs = process.argv.slice(2);

if (cmdArgs.length < 2) {
  console.log('wrong number of input arguments. requires at least 3');
  process.exit(98);
}

const writeFileAsync = (filePath, content, encoding) => {
  return new Promise((resolve, reject) => {
    fs.writeFile(filePath, `${content}`, encoding, (err, data) => {
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
    await writeFileAsync(cmdArgs[0], cmdArgs[1], 'utf8');
  } catch (err) {
    console.error(err);
  }
})();
