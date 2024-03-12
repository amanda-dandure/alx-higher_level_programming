#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nOccurrences = 0;
  for (let p = 0; p < list.length; p++) {
    if (searchElement === list[p]) {
      nOccurrences++;
    }
  }
  return nOccurrences;
};
