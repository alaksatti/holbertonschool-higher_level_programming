#!/usr/bin/node
// script prints 3 lines
const length = parseInt(process.argv.length);
if (length === 2) {
  console.log('No argument');
} else if (length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
