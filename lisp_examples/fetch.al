; First, run an HTTP server listening on port 8000, e.g.
;   $ deno run --allow-net javascript_examples/server_basic.ts
; Then run this Async Lisp script:
;   $ python3 async_lisp/interpreter.py lisp_examples/fetch.al

(fetch "http://localhost:8000" print)
