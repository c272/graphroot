# Graphroot
*A python script that quickly calculates the roots of a graph. Requires "parser" (Inbuilt Py3.7+)*

Graphroot is a script which allows you to automatically calculate the 2 roots of a graph. To configure the program, follow the steps below.

## Syntax
**Equations:**

Equations should be put in full Python syntax, as the script uses the in-built "compile" and "expr" libraries.
So, an example of a functioning equation would be:
`2*x+1+5*(2*x+x^2)`
The same equation, in invalid syntax, would be:
`2x+1+5(2x+x^2)`

So, coefficients need "*" to multiply them by X, and numbers before brackets also need a "*"

