#!/usr/bin/node
exports.esrever = function (list) {
  const newString = [];
  for (let i = list.length - 1; i >= 0; i--) {
    newString.push(list[i]);
  }
  return newString;
};
