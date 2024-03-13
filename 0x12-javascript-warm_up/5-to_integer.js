#!/usr/bin/node
const args = process.argv.slice(2);

if (!Number.isInteger(args)) {
  console.log('Not a number');
} else {
  (`My number: ${args}`);
}
