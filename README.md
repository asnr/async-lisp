# Async Lisp

An experiment to implement `async` and `await` keywords.

## Lisp syntax

Stolen from racket

```
; variable definition
(define var 1)

; function definition
(define (square x) (* x x))

; if
(if (> 2 3) "2 is bigger than 3" "3 is bigger than 2")

```


## HTTP client program

Callback style:

```
(define (print-body res) (get-body-callback res print))  ; print is a function
(fetch-callback "http://localhost:8000" print-body)
```

Promise style:

```
(then
  (then
    (fetch "http://localhost:8000")
    get-body)
  print)
  
; Permit the syntax sugar
(then
  (fetch "http://localhost:8000")
  get-body
  print)
```

Await style:

```
; Alternatively, could require `let*` style
(define res (await (fetch "http://localhost:8000")))
(define body (await (get-body res)))
(print body)
```


## Running the interpreter

From the project root directory:

```
$ python3 async_lisp/interpreter.py lisp_examples/print.el
```


## Running tests

From the `async_lisp` directory:

```
$ python3 -m unittest
```

