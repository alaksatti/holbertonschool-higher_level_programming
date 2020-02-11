#!/usr/bin/node
// import 'list' from 100-map.js
const dict = require('./101-data').dict;

const newdict = {};
let ids;
for (ids in dict) {
  if (!newdict[dict[ids]]) { newdict[dict[ids]] = []; }
  newdict[dict[ids]].push(ids);
}

console.log(newdict);
