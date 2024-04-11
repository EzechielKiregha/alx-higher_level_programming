#!/usr/bin/node

exports.esrever = function (list) {
  return list.reduceRight(function (arr, current) {
    arr.push(current);
    return arr;
  }, []);
};
