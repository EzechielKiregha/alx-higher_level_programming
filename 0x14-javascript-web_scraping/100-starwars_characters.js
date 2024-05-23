#!/usr/bin/node
// a script that displays the status code of a GET request.

const request = require('request');
const cmdArgs = process.argv.slice(2);

if (cmdArgs.length < 1) {
  process.exit(98);
}

const movieId = cmdArgs[0];

const fetchEndpoint = async (requestUrl) => {
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

const getMovie = async () => {
  return new Promise((resolve, reject) => {
    request(
      `https://swapi-api.alx-tools.com/api/films/${movieId}`,
      (err, res) => {
        if (err) {
          reject(err);
        }
        resolve(JSON.parse(res.body));
      }
    );
  });
};

(async () => {
  const movie = await getMovie();
  const characters = movie.characters;
  const characterRequests = characters.map((el) => fetchEndpoint(el));
  let characterResponse = await Promise.all(characterRequests);
  characterResponse = await Promise.all(characterResponse);
  characterResponse = characterResponse.map((res) => res.name);
  for (const res of characterResponse) {
    console.log(res);
  }
})();
