#!/usr/bin/node
// reverses a list

exports.esrever = function (list) {
  const arr = [];

  for (let i = list.length - 1, j = 0; i >= 0; i--, j++) { arr[j] = list[i]; }

  return arr;
};
