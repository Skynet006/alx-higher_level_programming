#!/usr/bin/node

const num = parseInt(process.argv[2]);
console.log(factorial(num));

function factorial (n) {
  if (!n) {
    return 1;
  }

  return n * factorial(n - 1);
}
