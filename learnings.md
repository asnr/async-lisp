# Learnings (ugh)

## 2 different ways of calling functions

Hypothesis: every compiler, interpreter, has at least two different implementations for calling functions. One is an implementation for calling functions in the language being implemented, and another for "native"/"foreign"/"primitive" functions. The latter will include at least everything the operating system exposes.

In async-lisp, this is the difference between `LispFunction` and `PythonFunction`. The `LispFunction` ultimately runs the function by calling the evaluator code (`_evaluate_element`), while `PythonFunction` runs the function by calling the underlying python function.

Other examples of a similar thing:
* C compilers compiling to x86 will compile a function written in C to the machine instructions `call`, taking the called function location as an operand, then `ret` (on the callee) along with [register fiddling](https://www.cs.virginia.edu/~evans/cs216/guides/x86.html#calling). By contrast, to [make a system call](https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/Syscall.html), the callee needs to put the ID of the desired system call in a register and then execute the `syscall` instruction.

### Implementation note

When implementing a language, try and abstract the difference from the rest of the implementation. See for example the `Function` interface in the Async Lisp interpreter.
