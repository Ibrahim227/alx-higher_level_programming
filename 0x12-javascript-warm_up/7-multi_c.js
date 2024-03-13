#!/usr/bin/node
const arg = process.argv[2];

const number = parseInt(arg);
const strVar = "C is fun";
if (!isNaN(number)) {
  console.log(`${number}` * `${strVar}`);
} else {
  console.log('Missing number of occurrences');
}
