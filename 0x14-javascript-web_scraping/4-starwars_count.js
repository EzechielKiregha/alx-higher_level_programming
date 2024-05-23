#!/usr/bin/node
// a script that prints the number of movies
// where the character “Wedge Antilles” is present.

const request = require('request');
const cmdArgs = process.argv.slice(2);
let requestUrl = 'https://swapi-api.alx-tools.com/api/films';

requestUrl = cmdArgs.length > 0 ? cmdArgs[0] : requestUrl;

const getMovies = async () => {
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
  const movie = await getMovies();
  if (movie.results && Array.isArray(movie.results)) {
    movie.results = movie.results.filter(result => result.characters.some(char => {
      const regTest = /.*18\/$/;
      return char.match(regTest);
    }));
  }
  console.log(movie.results.length);
})();
