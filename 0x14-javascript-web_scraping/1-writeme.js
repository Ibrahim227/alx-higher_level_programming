#!/usr/bin/node

const fs = require('fs');

function WriteStringToFile (filepath, content) {
    fs.writeFile(filepath, content + '\n', 'utf-8', (err) => {
	if (err) {
	  console.error(err);
	} else {
	  console.log('');
	}
    });
}

const filepath = process.argv[2];
const content = process.argv[3];

if (!filepath || !content) {
  console.error('Usage: ./1-writeme.js <filename.txt> <content to write to the file>');
  process.exit(1);
}

WriteStringToFile(filepath, content);
