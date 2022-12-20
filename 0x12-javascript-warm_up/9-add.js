#!/usr/bin/node

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

add(a, b);

function add (a, b) {
  console.log(a + b);
}
