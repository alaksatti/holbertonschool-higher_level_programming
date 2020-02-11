#!/usr/bin/node
// prints the number of arguments printed and its value
global.args = 0;

exports.logMe = function (item) {
  console.log(global.args + ': ' + item);
  global.args += 1;
};
