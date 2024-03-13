#!/usr/bin/node

function exeTime(x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

function strVar() {
  console.log("C is fun");
}

exeTime(x, strVar);
