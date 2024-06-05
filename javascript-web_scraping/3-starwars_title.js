#!/usr/bin/node
const req = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
req.get(url, (err, res) => {
  err ? console.log(err) : console.log(JSON.parse(res.body).title);
});
