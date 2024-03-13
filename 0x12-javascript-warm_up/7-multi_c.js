#!/usr/bin/node
const arg = parseInt(process.argv[2]);

const strVar = "C is fun";

if (!isNaN(arg)) {
  for (let i = 0; i < arg; i++) {
    console.log(`${arg}` * `${strVar}`);
  }
} else {
    console.log('Missing number of occurrences');
}
