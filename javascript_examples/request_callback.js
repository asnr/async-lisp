// Run server first:
//   $ deno run --allow-net basic.ts
// Then run:
//   $ node request_callback.js
const { request } = require('node:http');

const req = request("http://localhost:8000", {}, (res) => {
  res.on('data', (chunk) => {
    console.log(`BODY: ${chunk}`);
  });
});

req.end()
