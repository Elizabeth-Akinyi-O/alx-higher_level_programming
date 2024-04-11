#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduceRight(function (array, element) {
    array.push(element);
    return array;
  }, []);
};
