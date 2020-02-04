#!/usr/bin/node
// checks if first arg can be converted to int and prints it
const num = parseInt(process.argv[2]);
if (num) {
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}
