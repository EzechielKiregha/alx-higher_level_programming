#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, curr) => curr === searchElement ? count + 1 : count, 0);
};
