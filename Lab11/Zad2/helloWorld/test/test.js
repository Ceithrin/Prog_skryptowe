//Source:  https://codeforgeek.com/unit-testing-nodejs-application-using-mocha/
var supertest = require("supertest");
var chai = require('chai');
var expect = chai.expect;
chai.use(require('chai-json'));

// This agent refers to PORT where program is runninng.
var server = supertest.agent("http://localhost:3000");

// UNIT test begin
describe('GET /', function() {
      it('respond with html', function(done) {
         server
         .get('/')
         .expect('Content-Type', /html/)
         .expect(200, done);
      });
});

describe('GET /json/arytmetyka', function() {
    it('respond with html', function(done) {
       server
       .get('/json/arytmetyka')
       .expect('Content-Type', /html/)
       .expect(200, done);
    });
});

describe('Check arytmetyka.json', function () {
    it('is a json file', function (done) {
      expect('D:/Documents/Studia/Skryptowe/Repos/Prog_skryptowe/Lab11/Zad2/helloWorld/json/arytmetyka.json').to.be.a.jsonFile();
      done()
    });
});
   