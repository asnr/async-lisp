// Run:
//   $ node echo_callback.js
//
// Make request:
//   $ curl --data "beep boop" localhost:8000
//   > Hello world
const { createServer } = require('node:http');

const hostname = '127.0.0.1';
const port = 8000;

const server = createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  req.on('data', (chunk) => {
    res.write(`Here is the body: ${chunk.toString()}`);
    res.end();
  });
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
