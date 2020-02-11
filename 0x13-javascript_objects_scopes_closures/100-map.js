#!/usr/bin/node
// import 'list' from 100-map.js
const list = require('./100-data').list;

const newlist = list.map((x, index) => { return (x * index); });

console.log(list);
console.log(newlist);
