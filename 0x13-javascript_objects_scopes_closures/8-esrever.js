#!/usr/bin/node
exports.esrever = function (list) {
  let reversedList = [];
  let i;
  for (i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;
};
