#!/usr/bin/node
// Script that prints a message depending of the number of arugments passed
const args = process.argv.slice(2);
const msg = args.length === 0 ? 'No argument' : (args.length === 1 ? 'Argument found' : 'Arguments found');
console.log(msg);
