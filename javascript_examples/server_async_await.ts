// Start server:
//   $ deno run --allow-net basic_async.ts
//
// Make request
//   $ curl --data "beep boop" localhost:8000
//   > Here is the body: beep boop
Deno.serve(async (req) => {
  if (req.body) {
    const body = await req.text();
    return new Response(`Here is the body: ${body}`);
  }

  return new Response("body is empty");
});
