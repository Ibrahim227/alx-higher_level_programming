#!/usr/bin/node

const fs = require('fs');
let data = "Python is cool";

fs.writeFile("my_file.txt", data, (err) => {
    if (err) {
	console.log(err);
    } else {
	console.log("Success")
    }
});
