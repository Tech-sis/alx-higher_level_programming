#!/usr/bin/node
const argsC = process.argv.length - 2;
if (argsC === 0) {
  console.log('No argument');
} else if (argsC === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
