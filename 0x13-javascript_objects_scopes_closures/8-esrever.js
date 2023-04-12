#!/usr/bin/node
exports.esrever = function (list) {
  const i = list.length;
  const a = [];
  for (let j = i - 1; j >= 0; j--) {
    a.push(list[j]);
  }
  return a;
};
