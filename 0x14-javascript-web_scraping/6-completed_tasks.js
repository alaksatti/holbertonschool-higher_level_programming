#!/usr/bin/node
// computes the number of tasks completed by user id.

const request = require('request');
const URL = process.argv[2];

request(URL, { json: true }, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const dict = {};
    for (let i = 0; i < body.length; i++) {
      if (body[i].completed) {
        if (!(body[i].userId in dict)) {
          dict[body[i].userId] = 0;
        }
        dict[body[i].userId] += 1;
      }
    }
    console.log(dict);
  }
});
