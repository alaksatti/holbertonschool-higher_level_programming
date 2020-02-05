#!/usr/bin/node
// script that prints 3 lines
let num = process.argv[2];
if (num) {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
