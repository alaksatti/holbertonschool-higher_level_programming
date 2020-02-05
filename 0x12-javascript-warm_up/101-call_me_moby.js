#!/usr/bin/node
// script that computes and prints factorial
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
