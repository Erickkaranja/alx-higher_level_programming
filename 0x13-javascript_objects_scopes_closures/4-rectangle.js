#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      [this.width, this.height] = [w, h];
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) row += 'X';
      console.log(row);
    }
  }

  rotate () {
    const x = this.width;
    const y = this.height;
    this.width = y;
    this.height = x;
  }

  double () {
    const x = this.width;
    const y = this.height;
    this.width = x * 2;
    this.height = y * 2;
  }
};
