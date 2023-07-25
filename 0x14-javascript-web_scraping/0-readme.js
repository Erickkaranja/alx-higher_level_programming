#!/usr/bin/node

const fs = require('fs');
const FileName = process.argv[2];
fs.readFile(FileName, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
