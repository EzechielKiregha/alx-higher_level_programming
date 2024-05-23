#!/usr/bin/node
// a script that displays the status code of a GET request.

const request = require('request');
const cmdArgs = process.argv.slice(2);

if (cmdArgs.length < 1) { console.log('wrong input number of arguments. provide at least one'); }

const getMovieTitle = async () => {
  return new Promise((resolve, reject) => {
    request(
      `https://swapi-api.alx-tools.com/api/films/${cmdArgs[0]}`,
      (err, res) => {
        if (err) {
          reject(err);
        }
        resolve(res.body);
      }
    );
  });
};

(async () => {
  let movie = await getMovieTitle();
  movie = JSON.parse(movie);
  console.log(movie.title);
})();
