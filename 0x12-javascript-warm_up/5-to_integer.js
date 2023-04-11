#!/usr/bin/node
const entry = Math.floor(Number(process.argv[2]));
console.log(isNaN(entry) ? 'Not a number' : `My number: ${entry}`);
