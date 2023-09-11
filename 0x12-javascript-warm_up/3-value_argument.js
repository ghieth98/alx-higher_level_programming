#!/usr/bin/node
// Script that prints the first argument passed to it
const args = process.argv.slice(2);
const arg1 = args[0];

console.log(arg1 || 'No argument');
