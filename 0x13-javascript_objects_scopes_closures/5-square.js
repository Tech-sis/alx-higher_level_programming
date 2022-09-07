#!/usr/bin/node

const Rectangle = require('./3-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
