#!/usr/bin/node
/** script that prints a given message depending
   to the number of arguement passed**/
const count = process.argv.lengh;
console.log(count === 2 ? 'No argument' : count === 3 ? 'Argument found' : 'Arguments found');
