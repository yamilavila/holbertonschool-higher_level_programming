#!/usr/bin/node
"""Script that reads and prints the content"""

const fs = require('fs');
const fl = process.argv[2];

fs.readFl(fl, 'utf8', error);

function error (bad, data) {
	if (bad) {
		console.log(bad);
	} else {
	  process.stdout.write(data);
	}
}
