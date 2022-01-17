// No use of any template system
var express = require('express'),
    logger = require('morgan');
const fs = require('fs');
const path = require('path');
var app = express();
var x = 1;
var y = 2;

// Determining the contents of the middleware stack
app.use(logger('dev'));                         // Place an HTTP request recorder on the stack — each request will be logged in the console in 'dev' format
app.use(express.json());
// app.use(express.static(__dirname + '/public')); // Place the built-in middleware 'express.static' — static content (files .css, .js, .jpg, etc.) will be provided from the 'public' directory

// Route definitions
app.get('/', function (req, res) {     // The first route
    var x = 2;
    var y = 3;
    var answer =  x+y;
    res.send('<p> ' + x + " + " + y + " = " + answer + ' </p>');
});

function parse_op(op,x,y) {
    if (op == '+') {
        return x+y;
    }
    if (op == '-') {
        return x-y;
    }
    if (op == '*') {
        return x*y;
    }
    if (op == '/') {
        return x/y;
    }
}

app.get('/json/:name', (req,res) => {
    let data = fs.readFileSync(path.resolve(__dirname + "/json", req.params.name + '.json')); //__dirname - folder w którym jest obecnie, req.params.name - odnosi się do :name
    let arytmetyka = JSON.parse(data); // The JSON.parse() method parses a JSON string, constructing the JavaScript value or object described by the string. 

    var table = "<table border='1'><tr><th>x</th><th>Operation</th><th>y</th><th>Result</th></tr>"
    table += "---------------------------------------------------------------------------------"
    arytmetyka["aryt"].forEach( (data_op) => {  //wykonuje się dla każdego argumentu, po 3 - x, y, op
        
        var x = parseInt(data_op['x']);
        var y = parseInt(data_op['y']);
        var op = data_op['opertion'];
        var answer = parse_op(op,x,y); //funkcja
        table += "<tr>" //dodaje row
        table += "<td width=100px align='center'>" + x +"</td><td width=100px align='center'>" + op +"</td><td width=100px align='center'>" + y +"</td><td width=100px align='center'>" + answer +"</td></tr>";
        // table += "<tr></tr>"
    })
    table += "</table>";  
    res.send(table);
})


// The application is to listen on port number 3000
app.listen(3000, function () {
    console.log('The application is available on port 3000');
});