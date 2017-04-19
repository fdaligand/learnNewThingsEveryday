## Numbers, Dates and Times

### Rouding
> Use `round(value,ndigits)`. If `ndigits` is negative, rounding is made on tens, hundreds and so on.

### Performing Accurate Decimal Calculation

> Use `Decimal` module. It allows to control different aspect of calculations, including numbers of digits and rouding. 

```python
>>> a = 4.2
>>> b = 2.1
>>> a + b
6.300000000000001
>>> (a + b) == 6.3
False

# with Desimal module
>>> from decimal import Decimal
>>> a = Decimal('4.2')
>>> b = Decimal('2.1')
>>> a + b
Decimal('6.3')
>>> print(a + b)
6.3
>>> (a + b) == Decimal('6.3')
True

# change decimal context 
>>> from decimal import localcontext
>>> a = Decimal('1.3')
>>> b = Decimal('1.7')
>>> print(a / b)
0.7647058823529411764705882353
>>> with localcontext() as ctx:
... ctx.prec = 3
... print(a / b)
0.765
>>> with localcontext() as ctx:
... ctx.prec = 50
... print(a / b)
...
0.76470588235294117647058823529411764705882352941176
>>>
```

> Also use `math.fsum()` to avoid calculation errors when large numbers are summed with little one. See [limitations](https://docs.python.org/3/tutorial/floatingpoint.html) on Python documentation

```python
>>> nums = [1.23e+18, 1, -1.23e+18]
>>> sum(nums) # Notice how 1 disappears
0.0
>>> import math
>>> math.fsum(nums)
1.0
```

### Formating numbers

> The general form of the width and precision is `[<>^]?width[,]?(.digits)?`. Use of `%` is deprecated.

```python
>>> x = 1234.56789
>>> # Two decimal places of accuracy
>>> format(x, '0.2f')
'1234.57'
>>> # Right justified in 10 chars, one-digit accuracy
>>> format(x, '>10.1f')
' 1234.6'
>>> # Left justified
>>> format(x, '<10.1f')
'1234.6 '
>>> # Centered
>>> format(x, '^10.1f')
' 1234.6 '
>>> # Inclusion of thousands separator
>>> format(x, ',')
'1,234.56789'
>>> format(x, '0,.1f')
'1,234.6'
>>> # use e for exponential notation
>>> format(x, 'e')
'1.234568e+03'
>>> format(x, '0.2E')
'1.23E+03'
>>> # Also use in format notation
>>> 'The value is {:0,.2f}'.format(x)
'The value is 1,234.57'

```

### Binary, Octal and Hexadecimal Integers

> To convert an integer:
> * binary : use `bin()`or b with `format()`
> * octal : use `oct()`or o with `format()`
> * hexadecimal : use `hex()`or x with `format()`
> To convert string in different bases, use `int()` with an appropirate base 

### Complexe-Valued Math

> Complex numbers can be represented by `complex(real,img)`. Access individual value with `complex.real` `complex.imag`. All ususal operator work on it.

### Infinity and Nans

> Python define three kind of specific numbers, `inf`, `-inf` and `nan`. Use `math.isinf()` and `math.isnan()` to test this values. `NaN` value propagate through all operations without raising exceptions. 

```python
>>> a = float('inf')
>>> b = float('-inf')
>>> c = float('nan')
>>> a
inf
>>> b
-inf
>>> c
nan
# NaN never compare as equal.
>>> c = float('nan')
>>> d = float('nan')
>>> c == d
False
>>> c is d
False
```

### Fractions

> Python offers utility to make calcualtion easy with fraction through `fractions` module.

### calculating with Large Numerical Arrays, Matrix 

> For this specific kinf of calculation, us the `numpy` module rather than your own loop with call to `math` modules. See [Doucmentation on Numpy](http://www.numpy.org/) for more details.

### Generate randoms

> `random` module is make for that. To produce random integer, use `random.randint()`. For random floating point, use `random.random()`. Random is based on Mersenne Twister algorithm and is deterministic. This module also includes function for uniform, Gaussian and other probability distributions. **Do not use `random` for crypto program**.

```python
# picjk a random item 
>>> import random
>>> values = [1, 2, 3, 4, 5, 6]
>>> random.choice(values)
2
>>> random.choice(values)
3
>>> random.choice(values)
1

# Pick N items 
>>> random.sample(values, 2)
[6, 2]
>>> random.sample(values, 3)
[5, 4, 1]

# Shuffle values 
>>> random.shuffle(values)
>>> values
[2, 4, 6, 5, 3, 1]
>>> random.shuffle(values)
>>> values
[3, 5, 2, 1, 6, 4]
```

### Time convertion

> Use `datetime` and `timedelta` from `datetime` module for common calculations.

```python
>>> from datetime import timedelta
>>> a = timedelta(days=2, hours=6)
>>> b = timedelta(hours=4.5)
>>> c = a + b
>>> c.days
2
>>> c.seconds
37800
>>> c.seconds / 3600
10.5
>>> c.total_seconds() / 3600
58.5
>>> from datetime import datetime
>>> a = datetime(2012, 9, 23)
>>> print(a + timedelta(days=10))
2012-10-03 00:00:00
>>>
>>> b = datetime(2012, 12, 21)
>>> d = b - a
>>> d.days
89
>>> now = datetime.today()
>>> print(now)
2012-12-21 14:54:43.094063
>>> print(now + timedelta(minutes=10))
2012-12-21 15:04:43.094063
>>> a = datetime(2012, 3, 1)
>>> b = datetime(2012, 2, 28)
>>> a - b
datetime.timedelta(2)
>>> (a - b).days
2
>>> c = datetime(2013, 3, 1)
>>> d = datetime(2013, 2, 28)
>>> (c - d).days
1
```

> For more complex date manipulations, use `dateutil` module.

```python
>>> a = datetime(2012, 9, 23)
>>> a + timedelta(months=1)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'months' is an invalid keyword argument for this function
>>>
>>> from dateutil.relativedelta import relativedelta
>>> a + relativedelta(months=+1)
datetime.datetime(2012, 10, 23, 0, 0)
>>> a + relativedelta(months=+4)
datetime.datetime(2013, 1, 23, 0, 0)
>>>
>>> # Time between two dates
>>> b = datetime(2012, 12, 21)
>>> d = b - a
>>> d
datetime.timedelta(89)
>>> d = relativedelta(b, a)
>>> d
relativedelta(months=+2, days=+28)
>>> d.months
2
>>> d.days
28
```

> In case you need to get basic information about calendars, the `calendar` module can be useful.

### Converting string into Datetimes

> Use `datetime.strptime()` to do that. **Nevertheless**, it seems this function is very slow and should be replace by own made function if we know exactly the format of the date to convert.

```python
>>> from datetime import datetime
>>> text = '2012-09-20'
>>> y = datetime.strptime(text, '%Y-%m-%d')
>>> z = datetime.now()
>>> diff = z - y
>>> diff
datetime.timedelta(3, 77824, 177393)
# work in reverse
>>> z
datetime.datetime(2012, 9, 23, 21, 37, 4, 177393)
>>> nice_z = datetime.strftime(z, '%A %B %d, %Y')
>>> nice_z
'Sunday September 23, 2012'
```