"use strict";

var expect = chai.expect;

function sum(x,y) {
	return x+y;
}

describe('The sum() function', function() {
 it('Returns 4 for 2+2', function() {
   expect(sum(2,2)).to.equal(4);
 });
 it('Returns 0 for -2+2', function() {
   expect(sum(-2,2)).to.equal(0);
 });
});

var final_sum = 0

function cyfry(napis) {
  var numbers = ''
  for (let i = 0; i < napis.length; i++) {
    if (!isNaN(napis[i])) {
      numbers += napis[i]
    }
  }
  numbers = numbers.split('')
  var sum = 0;
  for (let i = 0; i < numbers.length; i++) {
    sum += parseInt(numbers[i]);
  }
  return sum
}



function litery(napis) {
  const regex = /[a-z]/g;
  var found = (napis.match(regex) || []).length;
  return found
}

function suma(napis) {
  var parsed = parseInt(napis)
  if (!isNaN(parsed))
    final_sum = final_sum + parsed
  return final_sum
}

describe('The cyfry() function', function() {
    it('Returns 3 for 111', function() {
      expect(cyfry('111')).to.equal(3);
    });
    it('Returns 0 for abc', function() {
      expect(cyfry('abc')).to.equal(0);
    });
    it('Returns 4 for abc31', function() {
        expect(cyfry('abc31')).to.equal(4);
    });
    it('Returns 4 for 31abc', function() {
        expect(cyfry('31abc')).to.equal(4);
      });
    it('Returns 0 for \'\'', function() {
        expect(cyfry('')).to.equal(0);
      });
   });

describe('The litery() function', function() {
    it('Returns 0 for 111', function() {
      expect(litery('111')).to.equal(0);
    });
    it('Returns 3 for abc', function() {
      expect(litery('abc')).to.equal(3);
    });
    it('Returns 3 for abc31', function() {
        expect(litery('abc31')).to.equal(3);
    });
    it('Returns 3 for 31abc', function() {
        expect(litery('31abc')).to.equal(3);
      });
    it('Returns 0 for \'\'', function() {
        expect(litery('')).to.equal(0);
      });
   });

describe('The suma() function', function() {
    it('Returns 111 for 111', function() {
      expect(suma('111')).to.equal(111);
    });
    it('Returns 111 for abc', function() {
      expect(suma('abc')).to.equal(111);
    });
    it('Returns 112 for abc1', function() {
        expect(suma('abc31')).to.equal(111);
    });
    it('Returns 142 for 31abc', function() {
        expect(suma('31abc')).to.equal(142);
      });
    it('Returns 142 for \'\'', function() {
        expect(suma('')).to.equal(142);
      });
   });