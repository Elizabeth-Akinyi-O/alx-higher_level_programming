#!/usr/bin/node
// Prints all characters of a Star Wars movie:
// The first argument is the Movie ID - example: 3 = “Return of the Jedi”
// Display one character name by line in the same order of the list “characters” in the /films/ response
// You must use the Star wars API

const request = require('request');
const MyFiles = process.argv.slice(2);
let data;
let i;
let MyList = [];
function GetCharId (id) {
  request('https://swapi-api.hbtn.io/api/films/' + id,
    async function (error, response, body) {
      if (error) console.error(error);
      else {
        data = JSON.parse(body);
        MyList = data.characters;
        for (i = 0; i < MyList.length; i++) {
          const name = await GetName(MyList[i]);
          console.log(name);
        }
      }
    });
}

function GetName (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) reject(error);
      else {
        resolve(JSON.parse(body).name);
      }
    });
  });
}
GetCharId(MyFiles[0]);
