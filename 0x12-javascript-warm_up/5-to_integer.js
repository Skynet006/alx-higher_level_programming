#!/usr/bin/node

const array = process.argv;
const num = parseInt(array[2]);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
