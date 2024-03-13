#!/usr/bin/node
const arg = process.argv[2];

const number = parseInt(arg);
const strVar = "C is fun";
while (number) {
  console.log(`${number}` * `${strVar}`);
}
console.log('Missing number of occurrences');

