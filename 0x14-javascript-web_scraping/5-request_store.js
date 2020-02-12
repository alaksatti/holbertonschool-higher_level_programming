#!/usr/bin/node
// gets the contents of a webpage and stores it in a file

let request = require('request');
let fs = require('fs');

request(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(process.argv[3], body, 'utf8', function (err) {
      if (err) {
        console.log(err);
      }});
  }});
