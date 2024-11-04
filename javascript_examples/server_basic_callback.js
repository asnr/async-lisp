// Run:
//   $ node basic_callback.js
//
// Make request:
//   $ curl localhost:8000
//   > Hello world
const { createServer } = require('node:http');

const hostname = '127.0.0.1';
const port = 8000;

const server = createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  // Note that this is equivalent to res.write("Hello world"); res.end();
  res.end('Hello World');
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
