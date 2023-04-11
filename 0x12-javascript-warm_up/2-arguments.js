#!/usr/bin/node

const { argv } = require('node:process');

const args = argv.slice(2);
const length = args.length;

if (length === 0) {
  console.log('No argument');
} else if (length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
