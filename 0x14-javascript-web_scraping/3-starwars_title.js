#!/usr/bin/node

const request = require('request');
let url = '' + process.argv[2];
request(url, function (error, response, body) {
  console.log(error || json.parse(body).title);
  });
