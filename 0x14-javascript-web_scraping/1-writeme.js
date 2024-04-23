#!/usr/bin/node

const fs = require('fs');

function WriteStringToFile (filepath, content) {
  try {
    fs.writeFileSync(filepath, content);
  } catch (err) {
    console.log(i'Error', err);
  }
}

const filepath = process.argv[2];
const content = process.argv[3];

if (!filepath || !content) {
  console.error('Usage: ./1-writeme.js <filename.txt> <content to write to the file>');
}

WriteStringToFile(filepath, content);
