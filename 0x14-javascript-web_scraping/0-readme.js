#!/usr/bin/node
/* Reads and prints the content of a file */

const fs = require('fs');

if (process.argv.length < 3) {
  console.error('File name is missing!');
  process.exit(1);
}

const fileName = process.argv[2];

fs.readFile(fileName, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  console.log(data);
});
