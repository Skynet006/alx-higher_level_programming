#!/usr/bin/node

let array = process.argv;

if (array.length === 2) {
  console.log(0);
} else if (array.length === 3) {
  console.log(0);
} else {
  array = array.splice(2);
  array = array.map(Number);
  const i = array.length;
  array.sort((a, b) => a - b);
  console.log(array[i - 2]);
}
