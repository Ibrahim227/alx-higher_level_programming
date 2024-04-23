#!/usr/bin/node

const fs = require('fs');

// Function to read and print file content
function readFileContent (filePath) {
  try {
    // Read file synchronously
    const content = fs.readFileSync(filePath, 'utf8');
    // Print file content
    console.log(content);
  } catch (err) {
    // Handle errors
    console.error('Error reading file:', err);
  }
}

// Provide the file path as a command line argument
const filePath = process.argv[2];

// Check if file path is provided
if (!filePath) {
  console.error('Please provide the file path as a command line argument.');
  process.exit(1);
}

// Read and print file content
readFileContent(filePath);
