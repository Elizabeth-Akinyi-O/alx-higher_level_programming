#!/usr/bin/node
// Gets the contents of a webpage and stores it in a file (loripsum)

const request = require('request');
const filesys = require('fs');

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    filesys.writeFile(process.argv[3], body, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
