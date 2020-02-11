#!/usr/bin/node
// concats 2 files
const fs = require('fs');

fs.writeFileSync(process.argv[4], fs.readFileSync(process.argv[2]) + '\n' + fs.readFileSync(process.argv[3]) + '\n');
