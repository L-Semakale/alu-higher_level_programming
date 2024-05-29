#!/usr/bin/node
function factorial(n) { // Added space before parentheses
  if (isNaN(n) || n < 0) return 1;
  if (n === 0) return 1;
  return n * factorial(n - 1);
}
console.log(factorial(parseInt(process.argv[2])));
