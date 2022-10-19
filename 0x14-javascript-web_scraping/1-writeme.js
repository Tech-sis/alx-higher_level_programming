#!/usr/bin/node

const filename = process.argv[2];
const data = process.argv[3];
const fs = require('fs');

fs.writeFile(filename, data, 'utf8', function (err) {
  if (err) {
    return console.log(err);
  }
});
