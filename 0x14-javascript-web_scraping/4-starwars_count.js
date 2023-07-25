#!/usr/bin/node

const request = require('request')
const url = process.argv[2]
request(url, function (error, response, body) {
  if (!error) {
    const result = json.parse(body).results;
    console.log(result.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
      }, 0));
   }
  });
