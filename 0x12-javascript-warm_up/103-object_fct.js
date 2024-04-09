#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

const increment = function () {
	this.value++;
}

myObject.incr = increment;

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
