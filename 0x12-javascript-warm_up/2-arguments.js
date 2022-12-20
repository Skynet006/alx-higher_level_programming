#!/usr/bin/node

const array = process.argv;

if (array.length < 3) {
  console.log('No argument');
} else if (array.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}