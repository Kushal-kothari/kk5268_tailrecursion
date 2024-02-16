# Recursion in Programming: Exploring Tail and Non-Tail Recursion

This repository contains implementations of factorial functions using both non-tail and tail recursion in Common Lisp and Python. The purpose of these implementations is to explore and understand how each programming language handles recursion and to determine which one supports tail recursion optimization.

## Implementations

### Common Lisp

- `factorial_non_tail(input_value)`: Calculates the factorial of `input_value` using non-tail recursion.
- `factorial_tail(input_value &optional (acc 1))`: Calculates the factorial using tail recursion with an accumulator.

### Python

- `custom_factorial(value)`: A non-tail recursive function that calculates the factorial of `value`.
- `custom_tail_factorial(number, accumulator=1)`: A tail recursive version of the factorial function using an accumulator.

## Testing

To test the implementations, you will need to have both Python and an implementation of Common Lisp (such as SBCL) installed on your system.

### Testing in Common Lisp

Load the `.lisp` files into your Common Lisp environment and call the functions with the desired input values.

For small values (e.g., 4):
```lisp
(factorial_non_tail 4) ; Non-tail recursion
(factorial_tail 4)     ; Tail recursion
```


Testing in Python
Run the .py files using a Python interpreter, or import the functions into an interactive Python shell and call them with the desired input values.

For small values (e.g., 4):

```python
custom_factorial(4)       # Non-tail recursion
custom_tail_factorial(4)  # Tail recursion
```

For large values (e.g., 99999):
```python
custom_factorial(99999)       # Non-tail recursion
custom_tail_factorial(99999)  # Tail recursion
```
# CONCLUSION:
In this assignment, we explored recursion by implementing factorial functions in SBCL (Common Lisp) and Python, focusing on non-tail and tail recursion. Our findings revealed that Common Lisp (SBCL) excels in tail recursion optimization, allowing for efficient recursive calls without the risk of stack overflow, even with large numbers. Python, however, does not inherently support tail recursion optimization, making it prone to stack overflow errors in deep recursive calls.

This comparison underscores the importance of choosing the right programming language based on its strengths and limitations, particularly for tasks requiring extensive recursion. While Lisp provides built-in support for tail recursion, making it ideal for such scenarios, Python's approach necessitates careful planning and limitations awareness.

