#!/usr/bin/node
const arg = parseInt(process.argv[2]);

if (!isNaN(arg)) {
  for (let i = 0; i < arg; i++) {
    for (let j = 0; j < arg; j++)
      console.log('X');
  }
} else {
  console.log('Missing Size');
}
