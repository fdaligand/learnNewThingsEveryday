# Iterators and Generators

## Manually Consuming an Iterator 
> To manually consume iterable, use the `next()` function and wait for the `StopIteration` exception to be raised. Alternatively, you can instruct `next(iterable,None)` to return None (or any other value) instead of an exeption.

```python
>>> items = [1, 2, 3]
>>> # Get the iterator
>>> it = iter(items) # Invokes items.__iter__()
>>> # Run the iterator
>>> next(it) # Invokes it.__next__()
1
>>> next(it)
2
>>> next(it)
3
>>> next(it)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
StopIteration
```

## Delegating Iteration

> Define an `__ietr__()` method in your class to delegate iterations. 

```python
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []
    def __repr__(self):
        return 'Node({!r})'.format(self._value)
    def add_child(self, node):
        self._children.append(node)
    def __iter__(self):
        return iter(self._children)
# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    for ch in root:
        print(ch)
# Outputs Node(1), Node(2)
```

## Creating New Iteration Patterns with Generators

> To create a **generator**, you need a `yield` statement in you function. A generator only runs in response to iteration aka `next()` function.

```python
>>> def countdown(n):
... print('Starting to count from', n)
... while n > 0:
... yield n
... n -= 1
... print('Done!')
...
>>> # Create the generator, notice no output appears
>>> c = countdown(3)
>>> c
<generator object countdown at 0x1006a0af0>
>>> # Run to first yield and emit a value
>>> next(c)
Starting to count from 3
3
>>> # Run to the next yield
>>> next(c)
2
>>> # Run to next yield
>>> next(c)
1
>>> # Run to next yield (iteration stops)
>>> next(c)
Done!
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
StopIteration
```

## Implementing the iteration protocol

> Iterator protocol requires `__iter__()` to return a special iterator that implement a `__next__()` operation and uses a `StopIteration` exception to signal completion. **Implementing such object is a messy affair**. **Define your iterator as a generator and be done with it**.

```python
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []
    def __repr__(self):
        return 'Node({!r})'.format(self._value)
    def add_child(self, node):
        self._children.append(node)
    def __iter__(self):
        return iter(self._children)
    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()
# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))
    for ch in root.depth_first():
        print(ch)
# Outputs Node(0), Node(1), Node(3), Node(4), Node(2), Node(5)
```

## Iterating in reverse

> Use built-in `reversed()` function. Reversed iteration only works in object with determinable size or if the object implement a `__reversed__()` function.
> Turn object to list if neither of these conditions is ok. **Turning an iterable into al list could consume a lot of memory if it's large**.

## Defining Generator Functions with Extra state
> If you want a generator to expose extra state to the user, don't forget that you can easily implement ia as a class, putting the generator function in the `__iter__()` method.

```python 
from collections import deque
class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)
    def __iter__(self):
        for lineno, line in enumerate(self.lines,1):
            self.history.append((lineno, line))
            yield line
    def clear(self):
    self.history.clear()
# usage 
with open('somefile.txt') as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')
```

**It might require an extra step of calling ietr() if you are going to drive iteartion manually**

```python
>>> f = open('somefile.txt')
>>> lines = linehistory(f)
>>> next(lines)
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: 'linehistory' object is not an iterator
>>> # Call iter() first, then start iterating
>>> it = iter(lines)
>>> next(it)
'hello world\n'
>>> next(it)
'this is a test\n'
```

## Taking a slice of an iterator 

> Use `itertool.isslice()`. It's important to to emphase that `isslice()` will comssume data on the supplied iterator.

```python
>>> def count(n):
... while True:
... yield n
... n += 1
...
>>> c = count(0)
>>> c[10:20]
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'generator' object is not subscriptable
>>> # Now using islice()
>>> import itertools
>>> for x in itertools.islice(c, 10, 20):
... print(x)
...
10
11
12
13
14
15
16
17
18
19
```

## Skipping the first part of an iterable
> Use the `itertools` module. `itertool.dropwhile()` take a function and an iterable. The returned iterator discard the first items in the sequence as long as the supplied function return `True`.

```python
>>> with open('/etc/passwd') as f:
... for line in f:
... print(line, end='')
...
##
# User Database
#
# Note that this file is consulted directly only when the system is running
# in single-user mode. At other times, this information is provided by
# Open Directory.
...
##
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0:System Administrator:/var/root:/bin/sh
...
>>> from itertools import dropwhile
>>> with open('/etc/passwd') as f:
... for line in dropwhile(lambda line: line.startswith('#'), f):
... print(line, end='')
...
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0:System Administrator:/var/root:/bin/sh
...
```

> If you happen to know the exact numbers of items you want to skip, then you can use `itertools.isslice()`. `None` on the below exemple indicate that we want everything beyond the first three items.

```python
>>> from itertools import islice
>>> items = ['a', 'b', 'c', 1, 4, 10, 15]
>>> for x in islice(items, 3, None):
... print(x)
...
1
4
10
15
```

## Iterating over all of the possible combinations or permutation

> Use `itertools.permutations()` to get sequence of tuples that rearranges all of the items into all possible permutations. You can give an optional lenght argument for a smaller permutation.

```python
>>> items = ['a', 'b', 'c']
>>> from itertools import permutations
>>> for p in permutations(items):
... print(p)
...
('a', 'b', 'c')
('a', 'c', 'b')
('b', 'a', 'c')
('b', 'c', 'a')
('c', 'a', 'b')
('c', 'b', 'a')
```

> Use `itertools.combinations()` to produce a sequence of combinations of items. Use `itertools.combination_with_replacement()` if you that a same item to be chosen more than once.

```python
>>> from itertools import combinations
>>> for c in combinations(items, 3):
... print(c)
...
('a', 'b', 'c')
>>> for c in combinations(items, 2):
... print(c)
...
('a', 'b')
('a', 'c')
('b', 'c')
>>> for c in combinations(items, 1):
... print(c)
...
('a',)
('b',)
('c',)

# itertools.combination_with_replacement()
>>> for c in combinations_with_replacement(items, 3):
... print(c)
...
('a', 'a', 'a')
('a', 'a', 'b')
('a', 'a', 'c')
('a', 'b', 'b')
('a', 'b', 'c')
('a', 'c', 'c')
('b', 'b', 'b')
('b', 'b', 'c')
('b', 'c', 'c')
('c', 'c', 'c')
```

## Iterating over the Index-Value Pairs of a sequence

> Use `enumerate()`. Can be cannonicale if `1` is passed as second arg. This case is especially useful for tracking line numbers in files should you want to use a line number in an error message. It should replace implementation of your own counter in function!

```python
def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[1])
                ...
            except ValueError as e:
                print('Line {}: Parse error: {}'.format(lineno, e))
# record world of text and save line appartition 
word_summary = defaultdict(list)
with open('myfile.txt', 'r') as f:
    lines = f.readlines()
for idx, line in enumerate(lines):
    # Create a list of words in current line
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)
# be aware of folling in tuple 
>>> data = [(1,2),(3,4),(5,6)]                                 
>>> for n,(x,y) in enumerate(data) : print(n,(x,y))            
...                                                            
0 (1, 2)                                                       
1 (3, 4)                                                       
2 (5, 6)                                                       
>>> for n,a in enumerate(data) : print(n,a)                    
...                                                            
0 (1, 2)                                                       
1 (3, 4)                                                       
2 (5, 6)                                                       
>>> for n,x,y in enumerate(data) : print(n,a)                  
...                                                            
Traceback (most recent call last):                             
  File "<stdin>", line 1, in <module>                          
ValueError: not enough values to unpack (expected 3, got 2)    
# Bonus: make a dict
>>> dict(enumerate(["a","b","c"]))
{0: 'a', 1: 'b', 2: 'c'}
```

## Iterating over multiple sequences Simultaneously 

> Use the `zip()` function. Use `itertools.zip_longest()` to iter over the longest item. You can pair the values together to make a dictionary. `zip()` accept more than two sequences. **`zip() create an iterator as result**

```python
>>> a = [1, 2, 3]
>>> b = ['w', 'x', 'y', 'z']
>>> for i in zip(a,b):
... print(i)
...
(1, 'w')
(2, 'x')
(3, 'y')
# zip_longest()
>>> from itertools import zip_longest
>>> for i in zip_longest(a,b):
...     print(i)
(1, 'w')
(2, 'x')
(3, 'y')
(None, 'z')
>>> for i in zip_longest(a, b, fillvalue=0):
...     print(i)
...
(1, 'w')
(2, 'x')
(3, 'y')
(0, 'z')

# make dict 
>>> dict(zip([1,2],(3,4)))
{1: 3, 2: 4}
```

## Iterating on Items in separate Containers

> Use `itertools.chain()`. Is more elegant than two different loop. It is also more efficient that adding to iterable (regarding memory) and don't raise error in different type.
 

```python

# chaining different object 
>>> a = [1,2]
>>> b = (3,4)
>>> for n in a + b : print n
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate list (not "tuple") to list
>>> from itertools import chain      
>>> for n in chain(a,b) : print(n)   
...                                  
1                                    
2                                    
3                                    
4                                    
```

## Creating Data Processing Pipelines

> Generators function are good way to implement processing pipeline. 
> A complete descrition and implementation of this mechanism is describe in recipe 4.113 of the book.
> See also [Generator Tricks for Systems Programmers](http://www.dabeaz.com/generators/) for further details.**To be read**

## Flattening a nested sequence

> Use recursive generators with a `yield from`.
> `yield from` is used to emit all of its values as a kind of subroutine. 

```python
from collections import Iterable
def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

items = [1, 2, [3, 4, [5, 6], 7], 8]
# Produces 1 2 3 4 5 6 7 8
for x in flatten(items):
    print(x)
```

> `ignore_type` is use to prevent string and byte from being interpreted as iterables. 

## Iterating in sorted order over merged sorted iterable

> Use `heapq.merge()`. It is important to emphasize that `heapq.merge()` requires that all input sequences albready be sorted.

```python
>>> import heapq
>>> a = [1, 4, 7, 10]
>>> b = [2, 5, 6, 11]
>>> for c in heapq.merge(a, b):
... print(c)
...
1
2
4
5
6
7
10
11
```

## Replacing infite while loops with an iterator 

> the following peace of code are the same 

```python
CHUNKSIZE = 8192
    def reader(s):
        while True:
            data = s.recv(CHUNKSIZE)
            if data == b'':
                break
            process_data(data)
# same code with iter method
def reader(s):
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
        process_data(data)
```

> The unknown feature of `iter()` function is that it optionally accepts a zero argument callable and a sentinel. It create an iterator that repeatedly calls the supplied callable over and over again until it returns the value given as a sentinel.

