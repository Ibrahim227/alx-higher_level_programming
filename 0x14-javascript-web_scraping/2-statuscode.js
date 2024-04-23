#!/usr/bin/node

const request = require('request');

function displayStatusCode (url) {
  request.get(url, (error, response) => {
    if (error) {
      console.error('Error:', error);
    } else {
      console.log('Succcess');
    }
  });
}

const url = process.argv[2];

if (!url) {
  console.error('Usage: ./2-statuscode <url>');
}

displayStatusCode(url);
