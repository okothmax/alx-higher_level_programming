#!/usr/bin/node
const values = process.argv.length;
console.log(values === 2 ? 'No argument' : values === 3 ? 'Argument found' : 'Arguments found');
