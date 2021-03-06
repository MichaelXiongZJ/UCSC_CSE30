# -*- coding: utf-8 -*-
"""Homework_12_feedback

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XTqjobtCYhfobnG1-a-IV4srv1GYgLTw

# Overall Score

You received 50 out of 70 points.

Before you turn this problem in, make sure everything runs as expected. First, **restart the kernel** (in the menubar, select Kernel$\rightarrow$Restart) and then **run all cells** (in the menubar, select Cell$\rightarrow$Run All).

Make sure you fill in any place that says `YOUR CODE HERE` or "YOUR ANSWER HERE", as well as your name and collaborators below:
"""

NAME = "Michael Xiong"
COLLABORATORS = ""

"""---

# CSE 30 Fall 2021 - Homework 12

## Cheapest Path


### Instructions

Please disregard the YOUR NAME and COLLABORATORS above.  They are put there atomatically by the grading tool.
You can find instructions on how to work on a homework on Canvas.  Here is a short summary: 

### Submitting your work

To submit your work: 

* First, click on "Runtime > Restart and run all", and check that you get no errors.  This enables you to catch any error you might have introduced, and not noticed, due to your running cells out of order. 
* Second, download the notebook in .ipynb format (File > Download .ipynb) and upload the .ipynb file to [this form](https://docs.google.com/forms/d/e/1FAIpQLSfRaOL643ZtXzI4R8TVpmfGoAcSjgLmXTEeUDqN0ZHoVNO6ow/viewform?usp=sf_link). 

You can submit multiple times; the last submission before the deadline is the one that counts.

### Homework format

For each question in this notebook, there is: 

* A text description of the problem. 
* One or more places where you have to insert your solution.  You need to complete every place marked: 

    `# YOUR CODE HERE`
    
    and you should not modify any other place. 
* One or more test cells.  Each cell is worth some number of points, marked at the top.  You should not modify these tests cells.  The tests pass if no error is printed out: when there is a statement that says, for instance: 

    `assert x == 2`
    
    then the test passes if `x` has value 2, and fails otherwise.  You can insert a `print(x)` (for this case!) somewhere if you want to debug your work; it is up to you.  
    
### Notes:

* Your code will be tested both according to the tests you can see (the `assert` statements you can see), _and_ additional tests.  This prevents you from hard-coding the answer to the particular questions posed.  Your code should solve the _general_ intended case, not hard-code the particular answer for the values used in the tests. 

* **Please do not delete or add cells!** The test is autograded, and if you modify the test by adding or deleting cells, even if you re-add cells you delete, you may not receive credit. 

* **Please do not import modules that are not part of the [standard library](https://docs.python.org/3/library/index.html).** You do not need any, and they will likely not available in the grading environment, leading your code to fail. 

* **If you are inactive too long, your notebook might get disconnected from the back-end.** Your work is never lost, but you have to re-run all the cells before you continue. 

* You can write out print statements in your code, to help you test/debug it. But remember: the code is graded on the basis of what it outputs or returns, not on the basis of what it prints.

* **TAs and tutors have access to this notebook,** so if you let them know you need their help, they can look at your work and give you advice. 

### Grading

Each cell where there are tests is worth a certain number of points.  You get the points allocated to a cell only if you pass _all_ the tests in the cell. 

The tests in a cell include both the tests you can see, and other, similar, tests that are used for grading only.  Therefore, you cannot hard-code the solutions: you really have to solve the essence of the problem, to receive the points in a cell. 

### Code of Conduct

* Work on the test yourself, alone. 
* You can search documentation on the web, on sites such as the Python documentation sites, Stackoverflow, and similar, and you can use the results. 
* You cannot share your work with others or solicit their help.

# Cheapest Path

In this notebook, we will implement an algorithm for finding the cheapest path between a source node and a destination node in a graph.  

For every node $x$, we will keep its set of successors $s(x)$, and its set of predecessors $p(x)$; these will be represented in code as dictionaries mapping nodes to sets of nodes.
Every edge $(x, y)$ (that is, going from $x$ to $y$) has a cost $c(x, y)$, which we will also keep as a dictinary mapping pairs of nodes to their cost. 

You can find the cheapest path in two steps.  

## Finding the minimum cost of going from every node to the destination

First, you need to compute the cost of going from every node to the destination.  In code, this happens in response to the method call 
`g.compute_cost(z)`, where `g` is the graph, and `z` is the destination. 
You can compute the minimum cost $c(x)$ of reaching the destination $z$ from a node $x$ as follows. 

Initially, you set $c(z) = 0$, and $c(x) = +\infty$ for all nodes $x \neq z$.  In Python, $+\infty$ is simply `float("inf")`, and yes, it's a number. 

Then, for all nodes $x \neq z$ with $s(x) \neq \emptyset$, you update $c(x)$ via: 

$$
c(x) := min_{y \in s(x)} [c(x, y) + c(y)] .
$$

You continue doing the above update until the costs no longer change. If you wish, you can do an optimization of the algorithm in which you only propagate change from the nodes whose cost has changed, as we did in the class notebook.  This is up to you. 

The initialization $c(x) = +\infty$ for $x \neq z$ ensures that nodes that _cannot_ get to $z$ will have infinite cost (as they should); if it were not for this, also using $c(x) = 0$ as initialization would work. 

You need to write a method `cost` so that `g.cost(x)` will return the cost $c(x)$ of node $x$; this will be useful in debugging (and grading) your code. 

## Finding the cheapest path 

The method `g.cheapest(w, z)` should return the list of nodes along the cheapest path from $w$ to $z$, starting from $w$, and ending with $z$, as a list. 

The method should first call `self.compute_cost(z)`, so that all the costs of nodes are known.  Then, the algorithm proceeds as follows.  First, as a sanity check, if $c(w) = +\infty$, you return `None` to indicate that there is no path.

Otherwise, the algorithm initializes the path $\sigma$ to $w$, as $\sigma = [w]$. 
Then, the algorithm picks the last state $x$ of $\sigma$, and repeatedly: 

* If $x = z$, we are done; we can return $\sigma$.
* Otherwise, we append to $\sigma$ the node $y \in s(x)$ such that $c(x, y) + c(y)$ is minimal. 

As edge costs are strictly positive, you don't need to worry about loops. 

This is it.  It's not too hard really, and it is quite related to the problem of timed scheduling as you see. 

Here is the class for the graph, with the methods for you to complete.
"""

from collections import defaultdict

# This is infinity.  Not kidding.
INFINITY = float("inf")

class PricedGraph(object):

    def __init__(self):
        self.s = defaultdict(set) # Successors
        self.p = defaultdict(set) # Predecessors
        self.c = {} # Cost of edges
        # Below you can put any other initialization you think is necessary.
        # YOUR CODE HERE
        self.nodes = set()

    def add_edge(self, x, y, c):
        """Adds an edge from x to y with cost c."""
        assert c > 0, "Costs need to be strictly positive."
        self.s[x].add(y)
        self.p[y].add(x)
        self.c[(x, y)] = c
        # Below, you can put any other thing you like to do.
        # YOUR CODE HERE
        self.nodes.add(x)
        self.nodes.add(y)

    def compute_cost(self, z):
        """Computes the minimum cost of reaching z from every node.
        Store this somewhere."""
        # YOUR CODE HERE
        self.c[z] = 0
        for a in self.nodes:
          if a is not z:
            self.c[a] = INFINITY
        for num_iteration in range(len(self.nodes)):
          condition = False
          for x in self.nodes:
            if x != z and self.s[x] != set():
              costs = [self.c[(x,y)] + self.c[y] for y in self.s[x]]
              condition = condition or self.c[x] != costs
              self.c[x] = min(costs)
          if not condition:
            break
 
    def cost(self, x):
        """Returns the cost of going from x to z.  You should have stored this
        cost somewhere in the above method compute_cost, for every x."""
        # YOUR CODE HERE
        return self.c[x]

    def cheapest_path(self, w, z):
        """Returns the cheapest path from w to z, as a list beginning with w
        and ending with z.  Note: you need to call self.cost(z) first thing
        inside the implementation of this method.  If you CANNOT reach z,
        which is indicated by w having infinite cost, return None."""
        # YOUR CODE HERE
        self.compute_cost(z)
        if self.c[w] == INFINITY:
          return None
        else:
          sigma = [w]
          x = sigma[-1]
          while sigma[-1] != z:
            min_cost = INFINITY
            min_node = INFINITY
            for y in self.s[x]:
              cost = self.c[x,y] + self.c[y]
              if min_cost > cost:
                min_cost = cost
                min_node = y
            sigma.append(min_node)
            x = sigma[-1]
          return sigma

"""Here you can play with your code. """

### Here you can play with your code.
g = PricedGraph()
g.add_edge('a', 'b', 2)
g.add_edge('b', 'c', 3)
g.add_edge('a', 'c', 6)
g.add_edge('d', 'a', 4)

g.compute_cost('c')
assert g.cost('c') == 0
assert g.cost('b') == 3
assert g.cost('a') == 5
print(g.cost('d'))
assert g.cost('d') == 9

"""### Testing the cost

Let's start trying how it works on simple examples.
"""

### For this question, you received 5 out of 5 points.

# 5 points

g = PricedGraph()
g.add_edge('a', 'b', 1)

# You can go from a to b
g.compute_cost('b')
assert g.cost('a') == 1
assert g.cost('b') == 0

# But you can't go from b to a.
g.compute_cost('a')
assert g.cost('a') == 0
assert g.cost('b') == INFINITY

"""Now, a tiny bit more complicated. """

### For this question, you received 5 out of 5 points.

# 5 points

g = PricedGraph()
g.add_edge('a', 'b', 2)
g.add_edge('b', 'c', 3)
g.add_edge('a', 'c', 6)
g.add_edge('d', 'a', 4)

g.compute_cost('c')
assert g.cost('c') == 0
assert g.cost('b') == 3
assert g.cost('a') == 5
assert g.cost('d') == 9

g = PricedGraph()
g.add_edge('a', 'b', 2)
g.add_edge('b', 'c', 3)
g.add_edge('a', 'c', 4)
g.add_edge('d', 'a', 4)

g.compute_cost('c')
assert g.cost('c') == 0
assert g.cost('b') == 3
assert g.cost('a') == 4
assert g.cost('d') == 8

### For this question, you received 2 out of 2 points.

# 2 points

# Let's take you for a loop.
g = PricedGraph()
g.add_edge('a', 'b', 2)
g.add_edge('b', 'c', 3)
g.add_edge('a', 'd', 1)
g.add_edge('d', 'a', 3)

g.compute_cost('c')
assert g.cost('c') == 0
assert g.cost('b') == 3
assert g.cost('a') == 5
assert g.cost('d') == 8

### For this question, you received 5 out of 5 points.

# 5 points

# Let's do the example from class.
g = PricedGraph()
g.add_edge('a', 'b', 2)
g.add_edge('a', 'c', 1)
g.add_edge('a', 'd', 2)
g.add_edge('b', 'e', 5)
g.add_edge('b', 'f', 1)
g.add_edge('c', 'b', 2)
g.add_edge('c', 'd', 3)
g.add_edge('d', 'f', 2)
g.add_edge('e', 'h', 2)
g.add_edge('f', 'g', 1)
g.add_edge('g', 'h', 2)

g.compute_cost('h')
assert g.cost('e') == 2
assert g.cost('f') == 3
assert g.cost('g') == 2
assert g.cost('b') == 4
assert g.cost('c') == 6
assert g.cost('d') == 5
assert g.cost('a') == 6

"""### Let's test the paths now."""

### For this question, you received 5 out of 5 points.

# 5 points

g = PricedGraph()
g.add_edge('a', 'b', 1)

assert g.cheapest_path('a', 'a') == ['a']
assert g.cheapest_path('a', 'b') == ['a', 'b']
assert g.cheapest_path('b', 'b') == ['b']
assert g.cheapest_path('b', 'a') == None

### For this question, you received 5 out of 5 points.

# 5 points

g = PricedGraph()
g.add_edge('a', 'b', 2)
g.add_edge('b', 'c', 3)
g.add_edge('a', 'c', 6)
g.add_edge('d', 'a', 4)

assert g.cheapest_path('a', 'c') == ['a', 'b', 'c']
assert g.cheapest_path('d', 'c') == ['d', 'a', 'b', 'c']
assert g.cheapest_path('d', 'b') == ['d', 'a', 'b']

g = PricedGraph()
g.add_edge('a', 'b', 2)
g.add_edge('b', 'c', 3)
g.add_edge('a', 'c', 4)
g.add_edge('d', 'a', 4)

assert g.cheapest_path('a', 'c') == ['a', 'c']
assert g.cheapest_path('d', 'c') == ['d', 'a', 'c']

### For this question, you received 3 out of 3 points.

# 3 points

g = PricedGraph()
g.add_edge('a', 'b', 2)
g.add_edge('b', 'c', 3)
g.add_edge('a', 'd', 1)
g.add_edge('d', 'a', 3)

assert g.cheapest_path('a', 'a') == ['a']
assert g.cheapest_path('d', 'd') == ['d']
assert g.cheapest_path('a', 'd') == ['a', 'd']
assert g.cheapest_path('a', 'c') == ['a', 'b', 'c']
assert g.cheapest_path('c', 'a') == None

### For this question, you received 5 out of 5 points.

# 5 points

# Let's do the example from class.
g = PricedGraph()
g.add_edge('a', 'b', 2)
g.add_edge('a', 'c', 1)
g.add_edge('a', 'd', 2)
g.add_edge('b', 'e', 5)
g.add_edge('b', 'f', 1)
g.add_edge('c', 'b', 2)
g.add_edge('c', 'd', 3)
g.add_edge('d', 'f', 2)
g.add_edge('e', 'h', 2)
g.add_edge('f', 'g', 1)
g.add_edge('g', 'h', 2)

assert g.cheapest_path('a', 'h') == ['a', 'b', 'f', 'g', 'h']
assert g.cheapest_path('c', 'h') == ['c', 'b', 'f', 'g', 'h']
assert g.cheapest_path('d', 'h') == ['d', 'f', 'g', 'h']

### For this question, you received 5 out of 5 points.

# 5 points

## Note that nodes can be anything.
g = PricedGraph()
g.add_edge(0, 1, 2)
g.add_edge(1, 2, 3)
g.add_edge(2, (3, 4), 4)
g.add_edge((3, 4), 4, 1)
assert g.cheapest_path(0, 4) == [0, 1, 2, (3, 4), 4]

"""## DO NOT MODIFY THE NOTEBOOK BELOW THIS LINE"""

### For this question, you received 0 out of 5 points.

## And now for some hidden tests.
# 5 points

### BEGIN HIDDEN TESTS
g = PricedGraph()
for i in range(10):
    g.add_edge((i, 0), (i + 1, 0), i + 1)
    g.add_edge((i, 1), (i + 1, 1), 10 - i)
    g.add_edge((i, 0), (i, 1), 1)
    g.add_edge((i, 1), (i, 0), 1)
assert g.cheapest_path((0, 0), (9, 0)) == [
    (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
    (5, 0), (5, 1), (6, 1), (7, 1), (8, 1),
    (9, 1), (9, 0)]
### END HIDDEN TESTS

### For this question, you received 0 out of 5 points.

# Hidden tests.  Do not remove this cell.
# 5 points
### BEGIN HIDDEN TESTS
g = PricedGraph()
for i in range(10):
    g.add_edge((i, 0), (i + 1, 0), i + 1)
    g.add_edge((i, 1), (i + 1, 1), 10 - i)
    g.add_edge((i + 1, 1), (i, 1), i + 1)
    g.add_edge((i, 0), (i + 1, 1), 10 - i)
    g.add_edge((i, 0), (i, 1), 1)
    g.add_edge((i, 1), (i, 0), 1)
assert g.cheapest_path((0, 0), (9, 0)) == [(0, 0), (1, 0), (2, 0), (3, 0),
    (4, 0), (5, 0), (6, 1), (7, 1), (8, 1), (9, 1), (9, 0)]
### END HIDDEN TESTS

### For this question, you received 0 out of 5 points.

# Hidden tests.  Do not remove this cell.
# 5 points
### BEGIN HIDDEN TESTS
g = PricedGraph()
for i in range(10):
    g.add_edge((i, 0), (i + 1, 0), i + 1)
    g.add_edge((i, 1), (i + 1, 1), 10 - i)
    g.add_edge((i, 0), (i, 1), 1)
    g.add_edge((i, 1), (i, 0), 1)
g.compute_cost((9, 0))
assert g.cost((3, 0)) == 25
assert g.cost((3, 1)) == 26
### END HIDDEN TESTS

### For this question, you received 5 out of 5 points.

# Hidden tests.  Do not remove this cell.
# 5 points
### BEGIN HIDDEN TESTS
g = PricedGraph()
for i in range(10):
    g.add_edge(i, (1 + i) % 10, 1 + i)
    g.add_edge((1 + i) % 10, i, 10 - i)
g.compute_cost(4)
d = {i: g.cost(i) for i in range(10)}
assert d == {0: 10, 1: 9, 2: 7, 3: 4, 4: 0, 5: 6, 6: 11, 7: 15, 8: 18, 9: 20}
### END HIDDEN TESTS

### For this question, you received 5 out of 5 points.

# Hidden tests.  Do not remove this cell.
# 5 points
### BEGIN HIDDEN TESTS
g = PricedGraph()
for i in range(10):
    g.add_edge(i, (1 + i) % 10, (3 * i) % 10 + 1)
    g.add_edge((1 + i) % 10, i, (7 * i) % 10 + 1)
assert g.cheapest_path(0, 7) == [0, 9, 8, 7]
assert g.cheapest_path(1, 7) == [1, 0, 9, 8, 7]
### END HIDDEN TESTS

### For this question, you received 0 out of 5 points.

# Hidden tests.  Do not remove this cell.
# 5 points
### BEGIN HIDDEN TESTS
g = PricedGraph()
for i in range(10):
    g.add_edge((i, 0), (i + 1, 0), i + 1)
    g.add_edge((i, 1), (i + 1, 1), 10 - i)
    g.add_edge((i, 0), (i, 1), 1)
    g.add_edge((i, 1), (i, 0), 1)
g.compute_cost((7, 1))
d = {i: g.cost((i, 0)) for i in range(10)}
assert d == {0: 25, 1: 24, 2: 22, 3: 19, 4: 15, 5: 10, 6: 5, 7: 1,
             8: INFINITY, 9: INFINITY}
### END HIDDEN TESTS