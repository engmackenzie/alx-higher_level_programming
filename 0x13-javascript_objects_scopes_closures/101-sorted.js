#!/usr/bin/js
let dict = require('./101-data').dict;
let newDict = {};
for (let key in dict) {
    if (newDict[dict[key]] === undefined) {
      newDict[dict[key]] = [];
    }
    newDict[dict[key]].push(key);
  }
  console.log(newDict);
