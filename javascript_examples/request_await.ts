// Run server first:
//   $ deno run --allow-net basic.ts
// Then
//   $ deno run --allow-net request_await.ts
const res = await fetch("http://localhost:8000");
const text = await res.text();
console.log(`Received response: ${text}`);
