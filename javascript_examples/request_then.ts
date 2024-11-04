// Run server first:
//   $ deno run --allow-net basic.ts
// Then
//   $ deno run --allow-net request_then.ts
fetch("http://localhost:8000")
  .then(res => res.text())
  .then(text => console.log(`Received response: ${text}`));
