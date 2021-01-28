var http = require('http');

http.createServer(function (req, res) {
    res.setHeader("Content-Type", "text/plain; charset=utf-8");
    let d = new Date();
    let timestamp = d.getTime();
    console.log(timestamp);
    res.end('Hello World!');
}).listen(9999);
