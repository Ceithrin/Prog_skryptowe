// Application using the 'Pug' template system
var express = require('express'),
    logger = require('morgan');
const fs = require('fs');
const path = require('path');
var app = express();
var x = 1;
var y = 2;

function sum(x, y) {
    return x + y
}

// Configuring the application
app.set('views', __dirname + '/views'); // Files with views can be found in the 'views' directory
app.set('view engine', 'pug');          // Use the 'Pug' template system

// Determining the contents of the middleware stack
app.use(logger('dev'));                         // Add an HTTP request recorder to the stack — every request will be logged in the console in the 'dev' format
// app.use(express.static(__dirname + '/public')); // Place the built-in middleware 'express.static' — static content (files .css, .js, .jpg, etc.) will be provided from the 'public' directory

// Route definitions
app.get('/', function (req, res) {      // The first route
    res.render('index', { x: x, y: y, operation: "+", result: x+y }); // Render the 'index' view in 'pretty' mode — the resulting HTML code will be indented — the 'pretty' option has the 'deprecated' status — in the future it will not be supported
    //res.render('index '); // Render the 'index' view; because the 'pretty' mode is, by default, turned off so the resulting HTML will be without indentation
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