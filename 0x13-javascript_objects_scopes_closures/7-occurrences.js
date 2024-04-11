#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((occurrences, element) => element === searchElement ? occurrences + 1 : occurrences, 0);
};
