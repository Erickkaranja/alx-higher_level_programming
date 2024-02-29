#!/usr/bin/node
/** prints a square**/
const a = Number(process.argv[1]);
for (let i = 0; i < a; i++) {
  let row = '';
  for (let j = 0; j < a; j++) {
    row += 'X';
  }
}
