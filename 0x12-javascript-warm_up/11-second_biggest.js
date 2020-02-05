#!/usr/bin/node
// search the second biggest integer
let arr = [];
let n = process.argv.length;
if (n < 4) {
  console.log(0);
} else {
  for (let i = 0; i < n ; i++) {
    if (parseInt(process.argv[i])) {
      arr.push(parseInt(process.argv[i]));
    }
  }
  arr = [...new Set(arr)].sort((a, b) => a - b);
  if (arr.length === 1) {
    console.log(arr[0]);
  } else {
    arr.pop();
    console.log(arr.pop());
  }
}
