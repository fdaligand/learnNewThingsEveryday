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

> Function also accept key parameter that allows them to be used with more complicated data structiures 

```python 
portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
```

### Implementing a priority queue
> Based on tuple comparison, heappush() and heappop
> * [Documentation](https://docs.python.org/3/library/heapq.html#priority-queue-implementation-notes)

### Mapping keys to Multiple Values in a Dictionary
>In principle, constructing a multivalued dictionary is simple. However, initialization of the first value can be messy if you try to do it yourself.

#### Simple way 
```python
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)
```
#### Pythonic way 
```python
from collections import defaultdict
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
```

### Keeping dictionaries in order
> **Be aware that the size of an OrderedDict is more than twice as large as a normal dictionary due to the extra linked list that’s created. Thus, if you are going to build a data structure involving a large number of OrderedDict instances (e.g., reading 100,000 lines of a CSV file into a list of OrderedDict instances), you would need to study the requirements of your application to determine if the benefits of using an OrderedDict outweighed the extra memory overhead.**

```python
from collections import OrderedDict
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    print(key, d[key])
```


### Calculating with dict

```python
prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}
min_price = min(zip(prices.values(), prices.keys()))
# min_price is (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys()))
# max_price is (612.78, 'AAPL')
prices_sorted = sorted(zip(prices.values(), prices.keys()))
# prices_sorted is [(10.75, 'FB'), (37.2, 'HPQ'),
# (45.23, 'ACME'), (205.55, 'IBM'),
# (612.78, 'AAPL')]
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names)) # OK
print(max(prices_and_names)) # ValueError: max() arg is an empty sequence
```

### Finding commonalities in two dict 

```python
a = {
'x' : 1,
'y' : 2,
'z' : 3
}
b = {
'w' : 10,
'x' : 11,
'y' : 2
}
# Find keys in common"
a.keys() & b.keys() # { 'x', 'y' }
# Find keys in a that are not in b
a.keys() - b.keys() # { 'z' }
# Find (key,value) pairs in common
a.items() & b.items() # { ('y', 2) }
# Make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
# c is {'x': 1, 'y': 2}
```

> `keys()` returns a keys-view object that support common `set` operation (union, intersection and difference). Idem for `items()`.
> Nevertheless, `values()` don't return a set like object ( value contained in dict are not guaranteed to be unique). Turn `values()` return to `set` to do same operation as `keys`.

### Removing duplicate from a sequence while maintaining order

> Sets are unordoned collection. To eliminate duplicate value in a sequence whil concerve order, use following tips:

#### Hashable sequence
```python
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

>>> a = [1, 5, 2, 1, 9, 1, 5, 10]
>>> list(dedupe(a))
[1, 5, 2, 9, 10]
```

#### Unhashable sequences
```python
def dedupe(items, key=None):
seen = set()
for item in items:
val = item if key is None else key(item)
if val not in seen:
yield item
seen.add(val)

>>> a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
>>> list(dedupe(a, key=lambda d: (d['x'],d['y'])))
[{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
>>> list(dedupe(a, key=lambda d: d['x']))
[{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
```

### Naming a slice

> Slicing data with magic number as index can be mess. As a general rule, writing code with a lot of hardcoded index values leads to a readability and maintenance mess.

```python
>>> items = [0, 1, 2, 3, 4, 5, 6]
>>> a = slice(2, 4)
>>> items[2:4]
[2, 3]
>>> items[a]
[2, 3]
>>> items[a] = [10,11]
>>> items
[0, 1, 10, 11, 4, 5, 6]
>>> del items[a]
>>> items
[0, 1, 4, 5, 6]
>>> a = slice(10, 50, 2)
>>> a.start
10
>>> a.stop
50
>>> a.step
2
```

### Determining the most frequentely occuring items in a sequence

> The `collections.Counter` class is designed for this task. Especially `most_common()` method

```python
words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]
from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)
# Outputs [('eyes', 8), ('the', 5), ('look', 4)]

morewords = ['why','are','you','not','looking','in','my','eyes']
>>> word_counts.update(morewords)
>>> a = Counter(words)
>>> b = Counter(morewords)
>>> a
Counter({'eyes': 8, 'the': 5, 'look': 4, 'into': 3, 'my': 3, 'around': 2,
"you're": 1, "don't": 1, 'under': 1, 'not': 1})
>>> b
Counter({'eyes': 1, 'looking': 1, 'are': 1, 'in': 1, 'not': 1, 'you': 1,
'my': 1, 'why': 1})
>>> # Combine counts
>>> c = a + b
>>> c
Counter({'eyes': 9, 'the': 5, 'look': 4, 'my': 4, 'into': 3, 'not': 2,
'around': 2, "you're": 1, "don't": 1, 'in': 1, 'why': 1,
'looking': 1, 'are': 1, 'under': 1, 'you': 1})
>>> # Subtract counts
>>> d = a - b
>>> d
Counter({'eyes': 7, 'the': 5, 'look': 4, 'into': 3, 'my': 2, 'around': 2,
"you're": 1, "don't": 1, 'under': 1})
>>>
```

### Sorting a list of dict by a common key 

> Use `itemgetter` from `operator` module

```python
from operator import itemgetter

rows = [
{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
print(rows_by_fname)
# [{'fname': 'Big', 'uid': 1004, 'lname': 'Jones'},
# {'fname': 'Brian', 'uid': 1003, 'lname': 'Jones'},
# {'fname': 'David', 'uid': 1002, 'lname': 'Beazley'},
# {'fname': 'John', 'uid': 1001, 'lname': 'Cleese'}]
print(rows_by_lfname)
# [{'fname': 'David', 'uid': 1002, 'lname': 'Beazley'},
# {'fname': 'John', 'uid': 1001, 'lname': 'Cleese'},
# {'fname': 'Big', 'uid': 1004, 'lname': 'Jones'},
# {'fname': 'Brian', 'uid': 1003, 'lname': 'Jones'}]

```

### Sorting object without native comparison support

> Use `attrgetter` (similary to `itemgetter`) as key parameter in the builtin function `sorted`. Can be used with multiple field. 

```python
>>> from operator import attrgetter
>>> class User:
... def __init__(self, user_id):
... self.user_id = user_id
... def __repr__(self):
... return 'User({})'.format(self.user_id)
...
>>> users = [User(23), User(3), User(99)]
>>> users
[User(23), User(3), User(99)]
>>> sorted(users, key=attrgetter('user_id'))
[User(3), User(23), User(99)]
```


### Grouping records together based on a field

> One way to do this is to use `itertools.groupby()` function. Be sure to sort item before appliying `groupby()` as this method only scan consecutive items.

```python 
rows = [
{'address': '5412 N CLARK', 'date': '07/01/2012'},
{'address': '5148 N CLARK', 'date': '07/04/2012'},
{'address': '5800 E 58TH', 'date': '07/02/2012'},
{'address': '2122 N CLARK', 'date': '07/03/2012'},
{'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
{'address': '1060 W ADDISON', 'date': '07/02/2012'},
{'address': '4801 N BROADWAY', 'date': '07/01/2012'},
{'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

from operator import itemgetter
from itertools import groupby
# Sort by the desired field first
rows.sort(key=itemgetter('date'))
# Iterate in groups
for date, items in groupby(rows, key=itemgetter('date')):
print(date)
for i in items:
print(' ', i)

# produce 
#07/01/2012
#    {'date': '07/01/2012', 'address': '5412 N CLARK'}
#    {'date': '07/01/2012', 'address': '4801 N BROADWAY'}
#07/02/2012
#    {'date': '07/02/2012', 'address': '5800 E 58TH'}
#    {'date': '07/02/2012', 'address': '5645 N RAVENSWOOD'}
#    {'date': '07/02/2012', 'address': '1060 W ADDISON'}
#07/03/2012
#    {'date': '07/03/2012', 'address': '2122 N CLARK'}
#07/04/2012
#    {'date': '07/04/2012', 'address': '5148 N CLARK'}
#    {'date': '07/04/2012', 'address': '1039 W GRANVILLE'}

```

**If random access is needed, use `defaultdict` instead of above receipe**

```python
from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)
>>> for r in rows_by_date['07/01/2012']:
... print(r)
{'date': '07/01/2012', 'address': '5412 N CLARK'}
{'date': '07/01/2012', 'address': '4801 N BROADWAY'}
>>>
```

### Filtering sequence Element
#### List comprehension 
```python
>>> mylist = [1, 4, -5, 10, -7, 2, 3, -1]
>>> [n for n in mylist if n > 0]
[1, 4, 10, 2, 3]
>>> [n for n in mylist if n < 0]
[-5, -7, -1]
>>>
```

#### generators 
```python
>>> pos = (n for n in mylist if n > 0)
>>> pos
<generator object <genexpr> at 0x1006a0eb0>
>>> for x in pos:
... print(x)
...
1
4
10
2
3
>>>
```

#### `filter()`

> If condition can't be expresses in a list comprehension or generators (check error handling for example)/ `Filter()` create an iterator, use `list()` if you want a list of result.

```python
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int, values))
print(ivals)
# Outputs ['1', '2', '-3', '4', '5']
```

#### `compress()`

> `itertools.compress()` takes an iterable and an accompanying Boolean selector sequence as input. As output, it gives you all of the items in the iterable where the corresponding element in the selector is True

```python
addresses = [
'5412 N CLARK',
'5148 N CLARK',
'5800 E 58TH',
'2122 N CLARK'
'5645 N RAVENSWOOD',
'1060 W ADDISON',
'4801 N BROADWAY',
'1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
>>> from itertools import compress
>>> more5 = [n > 5 for n in counts]
>>> more5
[False, False, True, False, False, True, True, False]
>>> list(compress(addresses, more5))
['5800 E 58TH', '4801 N BROADWAY', '1039 W GRANVILLE']
```


### Extracting a subset of dict 

#### Dictionnary comprehension

```python
prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}
# Make a dictionary of all prices over 200
p1 = { key:value for key, value in prices.items() if value > 200 }
# Make a dictionary of tech stocks
tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
p2 = { key:value for key,value in prices.items() if key in tech_names }
```

#### Tuple

```python
p1 = dict((key, value) for key, value in prices.items() if value > 200)
```

> dictionary comprehension solution is a bit clearer and actually runs quite
a bit faster (over twice as fast when tested on the ``prices dictionary used in the example)

### Mapping names to sequences elements

> Instead of access list or tuple elements by position, use 'collections.namedtuple()', that add min overhead to a tuple.
> * [Documentation](https://docs.python.org/3/library/collections.html#collections.namedtuple)

```python
>>> from collections import namedtuple
>>> Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
>>> sub = Subscriber('jonesy@example.com', '2012-10-19')
>>> sub
Subscriber(addr='jonesy@example.com', joined='2012-10-19')
>>> sub.addr
'jonesy@example.com'
>>> sub.joined
'2012-
```

```python 
def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total
# become 
from collections import namedtuple
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total
```

> Nametuple require less memory than dict. But, nametuple is immutable, you can change its value. To do so, use the `_replace` builtin method.

```python
>>> s = Stock('ACME', 100, 123.45)
>>> s
Stock(name='ACME', shares=100, price=123.45)
>>> s.shares = 75
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: can't set attribute
>>> s = s._replace(shares=75)
>>> s
Stock(name='ACME', shares=75, price=123.45)
```

### Transforming and reducing data at the same time

> Use generator expression without use of extra `()`. 

```python 
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)

s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# Data reduction across fields of a data structure
portfolio = [
{'name':'GOOG', 'shares': 50},
{'name':'YHOO', 'shares': 75},
{'name':'AOL', 'shares': 20},
{'name':'SCOX', 'shares': 65}
]

# Original: Returns 20
min_shares = min(s['shares'] for s in portfolio)
# Alternative: Returns {'name': 'AOL', 'shares': 20}
min_shares = min(portfolio, key=lambda s: s['shares'])
```

### Combining multiple mappings into a single mappings

#### `ChainMap()`

```python
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

from collections import ChainMap
c = ChainMap(a,b)
print(c['x']) # Outputs 1 (from a)
print(c['y']) # Outputs 2 (from b)
print(c['z']) # Outputs 3 (from a)

>>> len(c)
3
>>> list(c.keys())
['x', 'y', 'z']
>>> list(c.values())
[1, 2, 3]
```

#### `Update()`

```python
>>> a = {'x': 1, 'z': 3 }
>>> b = {'y': 2, 'z': 4 }
>>> merged = dict(b)
>>> merged.update(a)
>>> merged['x']
1
>>> merged['y']
2
>>> merged['
```

