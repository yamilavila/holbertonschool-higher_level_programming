#!/usr/bin/node
/*Task 3*/

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/:id' ;

request(url, + process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
