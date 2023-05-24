#!/usr/bin/node
/* Writes a string to a file */

const fs = require('fs');

if (process.argv.length < 4) {
  console.error('Usage: ./1-writeme.js "filepath" "string_to_write"');
  process.exit(1);
}

const fileName = process.argv[2];
const content = process.argv[3];

fs.writeFile(fileName, content, (err) => {
  if (err) {
    console.error(err);
    return;
  }

  console.log('Written successfully!');
});
