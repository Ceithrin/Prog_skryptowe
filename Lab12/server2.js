var fs = require("fs");

function onRequest_8080(request, response) {
    fs.stat(content, (err, stats) => {
        if (err == null) {
          fs.readFile(content, (err, data) => {
            response.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
            response.write(data);
            response.end();
          });
        }
        else {
          response.writeHead(200, { "Content-Type": "text/plain; charset=utf-8" });
          response.write('There was an error');
          response.end();
        }
      })
    }
  
  /* ************************************************** */
  /* Main block
  /* ************************************************** */
  var http = require('http');
  const content = 'zad2.html';
  
  http.createServer(onRequest_8080).listen(8080);
  console.log("The server was started on port 8080");
  console.log("To stop the server, press 'CTRL + C'");