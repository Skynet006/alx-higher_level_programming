#!/usr/bin/node

let num = parseInt(process.argv[2]);
let x = num;
let string = '';

if (isNaN(num)) {
  console.log('Missing size');
} else {
  while (x > 0) {
    string += 'X';
    x--;
  }

  while (num > 0) {
    console.log(string);
    num--;
  }
}
