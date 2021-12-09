"use strict";

// var expect = chai.expect;

function sum(x,y) {
	return x+y;
}

// describe('The sum() function', function() {
//  it('Returns 4 for 2+2', function() {
//    expect(sum(2,2)).to.equal(4);
//  });
//  it('Returns 0 for -2+2', function() {
//    expect(sum(-2,2)).to.equal(0);
//  });
// });

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

// var data = ''
// while (true) {
//     data = window.prompt('Podaj dane')

//     if (data == null)
//         break

//     console.log('\t' + cyfry(data) + '\t' + litery(data) + '\t' + suma(data))
// }

// desribe('funkcje', function() {

// })

var inp = '';
while (true){
    inp = window.prompt("Wpisz wartosc");
    if (inp == null) { break; };
    var a = cyfry(inp);
    var b = litery(inp);
    suma(inp);
    var out = document.getElementById("output");

    out.innerHTML += inp + "<br>" + "&emsp;<p style='color:red;'>" + a + "</p>" +
        "&emsp;<p style='color:green;'>" + b + "</p>" + 
        "&emsp;<p style='color:blue;'>" + final_sum + "</p>" + "<br>";

}