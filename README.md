# Algorithms

My implementation of some algortihms. The list of algorithms is continuously populated.
What's covered in this repository includes various approaches to solving algorithmic tasks. This includes the following important topics in computer science:
- [greedy algorithms](/greedy)
- [divide & conquer](/divide_and_conquer)
- [dynamic programming](/dynamic_programming)

The repository is continuously updated with new problems and solutions in various topics on algorithms.

### Greedy
This is a simple yet powerful technique: make an optimal (locally) step at each stage and gradually move towards solving the whole problem.
1. Make a first move. This should be a safe move, i.e. your greedy choice made here needs to be proved that it is in fact an optimal move (**you need to prove it to save debugging time!**).
2. Reduce it to a sub-problem of the same kind.
3. Continue until a trivial solution is found, i.e. it can be solved immediately.

### Divide-n-conquer
Main principle is to divide a problem into **disjoint** problems and tackle each separately until the solution is found. This is achieved by recursively calling these sub-problems.

### Dynamic Programming
Divide a problem into sub-problems and "optimize" recursive approach so that instead of calling recursive procedure you use the results precomputed before. This reduces the overall running time as comprared to recursive procedures.

## Misc problems

* calculation of the nth Fibonacci number (recursive [slow] and fast implementation [with memoization])
* determination of the remainder from division of the nth Fibonacci number by an integer
* merge sort
* checking for correctness of a parentheses sequence
* tree traversal (pre-order, in-order, post-order)
* finding greatest common divisor of two numbers
* finding least common multiple of two numbers
* last digit of the sum of Fibonacci numbers
* last digit of the partial sum of Fibonacci numbers
* last digit of the sum of squares of Fibonacci numbers
* remainder of the nth Fibonacci number

