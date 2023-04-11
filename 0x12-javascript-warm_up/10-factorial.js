#!/usr/bin/node

function factorize (n) {
  return n === 0 || isNaN(n) ? 1 : n * factorize(n - 1);
}

console.log(factorize(Number(process.argv[2])));
