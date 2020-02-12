#!/usr/bin/node
// prints the number of movies where the character “Wedge Antilles” is present.
const request = require('request');
const URL = process.argv[2];

request(URL, { json: true }, function (err, res, body) {
  if (err) { return (console.log(err)); }
  let count = 0;
  const data = body.results;
  for (let i = 0; i < data.length; i++) {
    const characters = data[i].characters;
    for (let k = 0; k < characters.length; k++) {
      if (characters[k].includes('/18/')) {
        count += 1;
        break;
      }
    }
  }
  console.log(count);
});
