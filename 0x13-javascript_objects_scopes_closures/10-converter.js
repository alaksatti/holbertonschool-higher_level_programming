#!/usr/bin/node
// converts a numer to another base
exports.converter = function (base) {
  return function conv (number) { return number.toString(base); };
};
