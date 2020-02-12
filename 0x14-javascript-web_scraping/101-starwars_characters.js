#!/usr/bin/node
const request = require('request');
const URL = 'https://swapi.co/api/films/' + process.argv[2];

request(URL, { json: true }, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const characters = body.characters;
    people(characters, 0);
  }
});

function people (characters, i) {
  if (characters[i] === undefined) { return; }
  request(characters[i], { json: true }, function (err, response, body) {
    if (err) {
      console.log(err);
    } else {
      console.log(body.name);
      people(characters, i + 1);
    }
  });
}
