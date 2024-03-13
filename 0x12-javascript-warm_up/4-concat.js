#!/usr/bin/node
const args = process.argv.slice(2);

if (!args.length) {
  console.log(undefined);
} else if (args.length === 1) {
  console.log(`${args} 'is' ${args}`);
} else {
  console.log('Arguments found');
}
