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