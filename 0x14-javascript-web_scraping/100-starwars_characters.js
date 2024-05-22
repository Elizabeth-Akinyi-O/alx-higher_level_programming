#!/usr/bin/node
// Prints all characters of a Star Wars movie:
// The first argument is the Movie ID - example: 3 = “Return of the Jedi”
// Display one character name by line. You must use the Star wars API

const request = require('request');
const movieId = process.argv[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(movieUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const movie = JSON.parse(body);
    const characters = movie.characters;
    // console.log(characters);
    for (const character of characters) {
      request.get(character, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          const names = JSON.parse(body);
          console.log(names.name);
        }
      });
    }
  }
});
