#!/usr/bin/node
const x = Math.floor(Number(process.argv[2]));
let y = 0;
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  while (y < x) {
    console.log('C is fun');
    y += 1
  }
}
