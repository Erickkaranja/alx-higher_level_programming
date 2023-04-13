#!/usr/bin/node
const fs = require('fs');

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destFile = process.argv[4];

// read the contents of the source file.
const file1Contents = fs.readFileSync(sourceFile1, 'utf8');
const file2Contents = fs.readFileSync(sourceFile2, 'utf8');

const concatenatedContents = file1Contents + file2Contents;

fs.writeFileSync(destFile, concatenatedContents);
