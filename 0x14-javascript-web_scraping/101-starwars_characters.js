#!/usr/bin/node
// prints all characters of a Star Wars movie
const request = require('request');
const request2 = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, (error, response, body) => {
  if (error) throw new Error(error);
  const characters = JSON.parse(body).characters;
  characters.forEach(character => {
    request2(character, (error, response, body) => {
      console.log(JSON.parse(body).name);
    });
  });
});
