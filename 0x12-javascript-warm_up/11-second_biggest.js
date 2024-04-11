#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const args = process.argv.slice(2).map(Number);
  const secBiggestInteger = args.sort(function (x, y) { return y - x; })[1];
  console.log(secBiggestInteger);
}
