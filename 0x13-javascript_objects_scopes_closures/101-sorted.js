#!/usr/bin/node

const dict = require('./101-data').dict;
const dkeys = Object.keys(dict);
const values = Object.values(dict);
let matched;
const result = {};
for (let a = 0; a < values.length; a++) { // loop
  result[JSON.stringify(values[a])] = [];
  matched = dkeys.filter(key => dict[key] === values[a]);
  matched.forEach(item => result[JSON.stringify(values[a])].push(item));
}
console.log(result);
