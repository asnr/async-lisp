;; hi there xorb

(define (print-me string-1 string-2) (print string-1 string-2))
(define (greeting string-1) (print-me "hi there" string-1))
(greeting "xorb")
