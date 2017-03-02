## Data structure and Algorithms

### Unpacking sequence into separate Variables
```python
p = (1,2)
x,y = p
>>> x
1
>>> y
2

>>> s = 'Hello'
>>> a, b, c, d, e = s
>>> a
'H'
>>> b
'e'
>>> e
'o'
>>>

>>> data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
>>> name, shares, price, (year, mon, day) = data
>>> name
'ACME'
>>> year
2012
>>> mon
12
>>> day
21
```
**Use _ for dummy variable to unpack**

### Unpacking Elements from iterables of arbitrary Length

>Use **star expression**. Variable declared with star will always be a list, even if unpacking of variable return None

```python
>>> a,*b = x
>>> a
1
>>> b
[2, 3]

>>> a,b,c,*d = x
>>> c
3
>>> d
[]

>>> line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
>>> uname, *fields, homedir, sh = line.split(':')
>>> uname
'nobody'
>>> homedir
'/var/empty'
>>> sh
'/usr/bin/false'
```

### Keeping the last N items

> Use **queue** from **collections** module. Using deque(maxlen=N) creates a fixed-sized queue. When new items are added and the queue is full, the oldest item is automatically removed.

```python
>>> q = deque(maxlen=3)
>>> q.append(1)
>>> q.append(2)
>>> q.append(3)
>>> q
deque([1, 2, 3], maxlen=3)
>>> q.append(4)
>>> q
deque([2, 3, 4], maxlen=3)
>>> q.append(5)
>>> q
deque([3, 4, 5], maxlen=3)

>>> q = deque()
>>> q.append(1)
>>> q.append(2)
>>> q.append(3)
>>> q
>>> deque([1, 2, 3])
>>> q.appendleft(4)
>>> q
deque([4, 1, 2, 3])
>>> q.pop()
3
>>> q
deque([4, 1, 2])
>>> q.popleft()
4
```

### Finding the largest or smallest N items

> Use **heapq**. The heapq module has two functions—nlargest() and nsmallest().
> Heaps are binary trees for which every parent node has a value less than or equal to any of its children.  The interesting property of a heap is that its smallest element is always the root, heap[0].
> * [Official Documentation](https://docs.python.org/3/library/heapq.html)
> * [Sam&Max](http://sametmax.com/heapq-le-module-python-incompris/)

```python
import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]
```
