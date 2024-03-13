#!/usr/bin/node
const arg = process.argv[2];

const number = parseInt(arg);
if (!isNaN(number)) {
  console.log(`${number} * C is fun`);
} else {
  console.log('Missing number of occurrences');
}
