#!/usr/bin/node

const fs = require('fs');

function WriteStringToFile (filepath, content) {
  try {
    fs.writeFileSync(filepath, content + '\n');
  } catch (err) {
    console.log('Error', err);
  }
}

const filepath = process.argv[2];
const content = process.argv[3];

if (!filepath || !content) {
  console.error('Usage: ./1-writeme.js <filename.txt> <content to write to the file>');
  process.exit(1);
}

WriteStringToFile(filepath, content);
