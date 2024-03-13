#!/usr/bin/node
const args = process.argv.slice[2];

const number = parseInt(arg);
if (!isNaN(number)) {
  console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}
