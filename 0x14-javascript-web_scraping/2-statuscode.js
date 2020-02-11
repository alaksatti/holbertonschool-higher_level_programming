#!/usr/bin/node
// display status code of get request
const request = require('request');

request(process.argv[2], { json: true }, function (err, res, body) {
  if (err) { return console.log(err); }
  console.log('code: ' + res.statusCode);
});
