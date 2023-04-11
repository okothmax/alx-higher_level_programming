#!/usr/bin/node
const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let width = 0; width < size; width++) {
    let joiner = '';
    for (let length = 0; length < size; length++) joiner += 'X';
    console.log(joiner);
  }
}
