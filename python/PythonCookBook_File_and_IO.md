# Files and I/O
## Reading and Writing Text Data

### `open()`

| mode | description |
| --- | --- |
| `r` | open for reading (default) |
| `w` | open for writing, truncating the file first |
| `x` | open for exclusive creation, failing if the file already exists |
| `a` | open for writing, appending to the end of the file if it exists |
| `b` | binary mode |
| `t` | text mode (default) |
| `+` | open a disk file for updating (reading and writing) |
| `U` | universal newlines mode (deprecated) |
> File read/write should be use with `with` statement to ensure context and closure of the file. We can supply a `newline` argrument to `open()`

```python
# On A UNIX machine 
>>> # Newline translation enabled (the default)
>>> f = open('hello.txt', 'rt')
>>> f.read()
'hello world!\n'
>>> # Newline translation disabled
>>> g = open('hello.txt', 'rt', newline='')
>>> g.read()
'hello world!\r\n'
>>>
```

> We can also manage encoding of the file with special argument `encoding`. You can also supply an optional argument `errors=replace|ignore|...`. See [Documentation](https://docs.python.org/3/library/functions.html#open) for more details.

## Redirect `print()` to file

```python
with open('somefile.txt', 'rt') as f:
print('Hello World!', file=f)
```


## Printing with different line endinf and separator

```python
>>> print('ACME', 50, 91.5)
ACME 50 91.5
>>> print('ACME', 50, 91.5, sep=',')
ACME,50,91.5
>>> print('ACME', 50, 91.5, sep=',', end='!!\n')
ACME,50,91.5!!

# Wrong usage of print 
>>> row = ('ACME', 50, 91.5)
>>> print(','.join(row))
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: sequence item 1: expected str instance, int found
>>> print(','.join(str(x) for x in row))
ACME,50,91.5
# Good usage exemple 
>>> print(*row, sep=',')
ACME,50,91.5
```

## Read/Write Binary Data (images,sounds,...)

> Just repalce `rt` by `rb` in `open()` function (as decribe above).

## Writing to a File That Doesn't already exist 

> In order to note erase file that already exist, use the `x` mode with `open()` 
> **Only exist in Python 3** (use `os.path.exists('somefile')` for Python2 )

```python
>>> with open('somefile', 'wt') as f:
... f.write('Hello\n')
...
>>> with open('somefile', 'xt') as f:
... f.write('Hello\n')
...
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
FileExistsError: [Errno 17] File exists: 'somefile'
```

## Performing I/O Operations on a string

> Use `io.StringIO()` or `io.BytesIO()` to create a file like object. Can be useful for unit testing. Be aware that these instance will not ahve a proper interger file descriptor. 

```python
>>> s = io.StringIO()
>>> s.write('Hello World\n')
12
>>> print('This is a test', file=s)
15
>>> # Get all of the data written so far
>>> s.getvalue()
'Hello World\nThis is a test\n'
>>>
>>> # Wrap a file interface around an existing string
>>> s = io.StringIO('Hello\nWorld\n')
>>> s.read(4)
'Hell'
>>> s.read()
'o\nWorld\n'

>>> s = io.BytesIO()
>>> s.write(b'binary data')
>>> s.getvalue()
b'binary data'
```


## Reading and Writing compressed datafiles

> To read/write on file with gzip or bz2 compression, use `gzip` and `bz2` modules. `gzip.opzn()` and `bz2.open()` accept the same parameters as the built-in `open()`. You can specify the compression level with `compressed`.

```python
# gzip compression
import gzip
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()
# bz2 compression
import bz2
with bz2.open('somefile.bz2', 'rt') as f:
    text = f.read()
# gzip compression
import gzip
with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)
# bz2 compression
import bz2
with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)
with gzip.open('somefile.gz', 'wt', compresslevel=5) as f:
    f.write(text)
```

## Iterating over Fixed-Sized Records

> Use the `iter()` function and `functools.partial()`.
> As already explain, `iter()` can create an iterator if you pass it a callable and a sentinel. `functools.partial` create a callable that reads a fixed number of **bytes** (open file in binary mode).

```python
from functools import partial
RECORD_SIZE = 32
with open('somefile.data', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        ...
```

## Memory mapping a binary file

> See description at chapetr 5.10 or read the [doc](https://docs.python.org/3/library/mmap.html) on `mmap`.

## Manipulating Pathnames

> Use function provided by `os.path` module. See [Documentation](https://docs.python.org/3/library/os.path.html?highlight=os.path#module-os.path)
for full reference

```python
>>> import os
>>> path = '/Users/beazley/Data/data.csv'
>>> # Get the last component of the path
>>> os.path.basename(path)
'data.csv'
>>> # Get the directory name
>>> os.path.dirname(path)
'/Users/beazley/Data'
>>> # Join path components together
>>> os.path.join('tmp', 'data', os.path.basename(path))
'tmp/data/data.csv'
>>> # Expand the user's home directory
>>> path = '~/Data/data.csv'
>>> os.path.expanduser(path)
'/Users/beazley/Data/data.csv'
>>> # Split the file extension
>>> os.path.splitext(path)
('~/Data/data', '.csv')
```

## Testing for File Existence

> Also through `os.path`

```python
>>> import os
>>> os.path.exists('/etc/passwd')
True
>>> os.path.exists('/tmp/spam')
False
>>> # Is a regular file
>>> os.path.isfile('/etc/passwd')
True
>>> # Is a directory
>>> os.path.isdir('/etc/passwd')
False
>>> # Is a symbolic link
>>> os.path.islink('/usr/local/bin/python3')
True
>>> # Get the file linked to
>>> os.path.realpath('/usr/local/bin/python3')
'/usr/local/bin/python3.3'
>>> os.path.getsize('/etc/passwd')
3669
>>> os.path.getmtime('/etc/passwd')
1272478234.0
>>> import time
>>> time.ctime(os.path.getmtime('/etc/passwd'))
'Wed Apr 28 13:10:34 2010'
```

## Getting directory listing 

> Use the `os.listdir()` To filter data use list comprehension combined with function from `os.path`. For filename matching, use `glob.glob()` or `fnmatch()`.

```python
import os.path
# Get all regular files
names = [name for name in os.listdir('somedir')
          if os.path.isfile(os.path.join('somedir', name))]
# Get all dirs
dirnames = [name for name in os.listdir('somedir')
            if os.path.isdir(os.path.join('somedir', name))]
pyfiles = [name for name in os.listdir('somedir')
            if name.endswith('.py')]
```
