#!/usr/bin/node
const arg = process.argv[2];

const number = parseInt(arg);
const strVar = "C is fun";

for (let i = 0; i < number; i++) {
  console.log(`${number}` * `${strVar}`);
}
console.log('Missing number of occurrences');

