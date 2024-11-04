// Run:
//   $ deno run --allow-net basic.ts
Deno.serve((_req) => {
  return new Response("Hello, World!");
});
