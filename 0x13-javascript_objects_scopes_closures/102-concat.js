#!/usr/bin/node
const fs = require('fs');
const i = fs.readFileSync(process.argv[2], 'utf8');
const j = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], i + j);
