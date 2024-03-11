#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const x = Number(process.argv[2]);
  let p = 0;
  while (p < x) {
    console.log('X'.repeat(x));
    p++;
  }
}
