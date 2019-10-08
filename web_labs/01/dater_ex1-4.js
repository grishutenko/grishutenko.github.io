#!/usr/bin/nodejs
(async r =>{
	const execFile = require('util').promisify(require('child_process').execFile);
	const { stdout } = await execFile('date');
	console.log(stdout);
	}
)();
