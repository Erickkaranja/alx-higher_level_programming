#!/usr/bin/node
/** script that prints a given message depending
   to the number of arguement passed**/

if (process.argv.length <= 2) {
  console.log('No argument');
} else if (process.argv.lengh === 3) {
  console.log('Argument found');
} else console.log('Arguments found');
