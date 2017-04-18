## String and Text

### Spliting String on Any Multiple Delimiters

#### `re.split()`

```python 
>>> line = 'asdf fjdk; afed, fjek,asdf, foo'
>>> import re
>>> re.split(r'[;,\s]\s*', line)
['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

>>> fields = re.split(r'(;|,|\s)\s*', line)
>>> fields
['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']
>>> values = fields[::2]
>>> delimiters = fields[1::2] + ['']
>>> values
['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
>>> delimiters
[' ', ';', ',', ',', ',', '']
>>> # Reform the line using the same delimiters
>>> ''.join(v+d for v,d in zip(values, delimiters))
'asdf fjdk;afed,fjek,asdf,foo'
>>>
# (?:...) means "noncapture group"
>>> re.split(r'(?:,|;|\s)\s*', line)
['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
>>>
```

### Matching text at the start or end of a string

> Use `str.startswith()` or `str.endswith()` function. For multiple choice, provide a `tuple()` (**mandatory**).


```python
>>> import os
>>> filenames = os.listdir('.')
>>> filenames
#[ 'Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h' ]
>>> [name for name in filenames if name.endswith(('.c', '.h')) ]
#['foo.c', 'spam.c', 'spam.h'
>>> any(name.endswith('.py') for name in filenames)
True
```

### Matching strings using shell wildcard patterns

> the `fnmatch` module provide two function `fnmatch()` and `fnmatchcase()`.
> `fnmatch()` is case sensitive. 

```python
>>> from fnmatch import fnmatch, fnmatchcase
>>> fnmatch('foo.txt', '*.txt')
True
>>> fnmatch('foo.txt', '?oo.txt')
True
>>> fnmatch('Dat45.csv', 'Dat[0-9]*')
True
>>> names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
>>> [name for name in names if fnmatch(name, 'Dat*.csv')]
['Dat1.csv', 'Dat2.csv']
```

> These function can be use for data processing.

```python
addresses = [
'5412 N CLARK ST',
'1060 W ADDISON ST',
'1039 W GRANVILLE AVE',
'2122 N CLARK ST',
'4802 N BROADWAY',
]
>>> from fnmatch import fnmatchcase
>>> [addr for addr in addresses if fnmatchcase(addr, '* ST')]
['5412 N CLARK ST', '1060 W ADDISON ST', '2122 N CLARK ST']
>>> [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]
['5412 N CLARK ST']
```

### Matching and searching for text patterns

> For simpel match, use `str.startswith()`, `str.endswith()` or `str.find()`. For more complicated search, use regular expression. If you made a lot of search with same pattern, use `re.compile()` to make a pattern. `match()` only return the first occurence of the pattern. `findall()` return all occurences. Use `finditer()` for iterative match.

```python
>>> datepat = re.compile(r'\d+/\d+/\d+')
>>> text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
>>> datepat.findall(text)
['11/27/2012', '3/13/2013']
```

```python
>>> m = datepat.match('11/27/2012')
>>> m
<_sre.SRE_Match object at 0x1005d2750>
>>> # Extract the contents of each group
>>> m.group(0)
'11/27/2012'
>>> m.group(1)
'11'
>>> m.group(2)
'27'
>>> m.group(3)
'2012'
>>> m.groups()
>>> ('11', '27', '2012')
>>> month, day, year = m.groups()
>>>
>>> # Find all matches (notice splitting into tuples)
>>> text
'Today is 11/27/2012. PyCon starts 3/13/2013.'
>>> datepat.findall(text)
[('11', '27', '2012'), ('3', '13', '2013')]
>>> for month, day, year in datepat.findall(text):
... print('{}-{}-{}'.format(year, month, day))
...
2012-11-27
2013-3-13
>>>
```

### Searching and replacing text

> Use `str.replace()` for simple litteral pattern.

```python
>>> text = 'yeah, but no, but yeah, but no, but yeah'
>>> text.replace('yeah', 'yep')
'yep, but no, but yep, but no, but yep'
>>>
```

> Use `re.sub()` for more sofisticated pattern. Backslashed digit refer to capture group numbers in the pattern. As above, use `re.compile` if you use same pattern multiple time. 

```python
>>> text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
>>> import re
>>> re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
'Today is 2012-11-27. PyCon starts 2013-3-13.'
>>>
```

> You can use callback with `re.sub()` for more complex pattern substitution

```python
>>> from calendar import month_abbr
>>> def change_date(m):
... mon_name = month_abbr[int(m.group(1))]
... return '{} {} {}'.format(m.group(2), mon_name, m.group(3))
...
>>> datepat.sub(change_date, text)
'Today is 27 Nov 2012. PyCon starts 13 Mar 2013.'
```

> Use `re.subn()` if you want to know the number of substitution performed.

### Be case insensitive in regex

> Use the flag `re.IGNORECASE` to perform case-insensitive match. 

```python 
>>> text = 'UPPER PYTHON, lower python, Mixed Python'
>>> re.findall('python', text, flags=re.IGNORECASE)
['PYTHON', 'python', 'Python']
>>> re.sub('python', 'snake', text, flags=re.IGNORECASE)
'UPPER snake, lower snake, Mixed snake'

# Enhanced function 
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
        return replace

>>> re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
'UPPER SNAKE, lower snake, Mixed Snake'
```

### Make regex non greedy

> Add `?` after the `*` operator in the pattern

```python
>>> text2 = 'Computer says "no." Phone says "yes."'
>>> str_pat = re.compile(r'\"(.*?)\"')
>>> str_pat.findall(text2)
['no.', 'yes.']
```

### Writing a regular expression for multiple patterns

> Match a block of text can be tricky with regex. As `.` match any charcater but not newline. To add support of newlines, use `(?:.|\n)`.
> See [Documentation](https://docs.python.org/3/library/re.html) for more info in this topic. You can also use `re.DOTALL` for simple case.

```python
text2 = '''/* this is a
... multiline comment */
... '''
>>> comment = re.compile(r'/\*((?:.|\n)*?)\*/')
>>> comment.findall(text2)
[' this is a\n multiline comment ']
>>>
```

### Normalizing Unicode Text to a Standard Representation

> The caractère `ñ` can be coded directly with unicode charactere `\u00F1` or can be a `n`+` ̃ ` (`\u0303`). If you compare two string with two different unicode, result will be false. We should normalize the text before string comparison. Use module `unicodedata` to do that. You have the choice between two type of normalization, `NFC`(characteres fully composed) or `NFD` (combining charactere). Python also support `NFKC` and `NFKD`.

### Unicode in regular expression 
```python
>>> import re
>>> num = re.compile('\d+')
>>> # ASCII digits
>>> num.match('123')
<_sre.SRE_Match object at 0x1007d9ed0>
>>> # Arabic digits
>>> num.match('\u0661\u0662\u0663')
<_sre.SRE_Match object at 0x101234030>
```

### Stripping Unwanted Char
> Use the `strip()` method to remove character from begiining or end of a string (use `lstrip()` or `rstrip()` for specific size. Argument of `strip()` is not a pattern but a list of character to remove. 

```python
>>> '   spacious   '.strip()
'spacious'
>>> 'www.example.com'.strip('cmowz.')
'example'
```

**Use generators to sanitize text from file**.
It’s efficient because it doesn’t actually read the data into any kind of temporary list first. It just creates an iterator where all of the lines produced have the stripping operation applied to them.
```python
with open(filename) as f:
    lines = (line.strip() for line in f)
    for line in
        ...
```

### Aligning Text String
> Use `ljust()`, `rjust()` and `center()`. These methods accept argument of **one character long**

```python
>>> text.rjust(20,'=')
'=========Hello World'
>>> text.center(20,'*')
'****Hello World*****'
>>>
```

> You can also use `format()` to align text.

```python
>>> format(text, '>20')
' Hello World'
>>> format(text, '<20')
'Hello World '
>>> format(text, '^20')
' Hello World '

# With file caracter
>>> format(text, '=>20s')
'=========Hello World'
>>> format(text, '*^20s')
'****Hello World*****'

# Multiple values

>>> '{:>10s} {:>10s}'.format('Hello', 'World')
' Hello World'

```

> `format()` is not strings specific

```python
>>> x = 1.2345
>>> format(x, '>10')
' 1.2345'
>>> format(x, '^10.2f')
' 1.23 '
```

### Combining and concatenating strings
> You can use `join()`, or `+` operator for simple strings. The most important thing to know is that using the + operator to join a lot of strings together is grossly inefficient due to the memory copies and garbage collection that occurs. 


### Interpolating Variables in Strings
> You can use `format()`, `format_map()` combined with `vars()`. Nevertheless, these methods don't deal gracefully with missing values. A way to avoid that is to declare a `dict` class with `__missing__()` methods.

```python
>>> s = '{name} has {n} messages.'
>>> s.format(name='Guido',n=37)
'Guido has 37 messages.'

# with format-map() and vars()
>>> name = 'Guido'
>>> n = 37
>>> s.format_map(vars())
'Guido has 37 messages.'

# Works with instance
>>> class Info:
... def __init__(self, name, n):
... self.name = name
... self.n = n
...
>>> a = Info('Guido',37)
>>> s.format_map(vars(a))
'Guido has 37 messages.'
>>>

# raise error on missing values 
>>> s.format(name='Guido')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
KeyError: 'n'
>>>

# create a class(dict) with __missing__ method to solve issue
class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

>>> del n # Make sure n is undefined
>>> s.format_map(safesub(vars()))
'Guido has {n} messages.'
>>>

# for frequent call to this kinf of algo 
import sys
def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))
>>> name = 'Guido'
>>> n = 37
>>> print(sub('Hello {name}'))
Hello Guido
>>> print(sub('You have {n} messages.'))
You have 37 messages.
>>> print(sub('Your favorite color is {color}'))
Your favorite color is {color}

```

### Handling HTML and XML Entities in Text
> use module `html` and its method `escape()` for escaping HTML charactere

```python
>>> s = 'Elements are written as "<tag>text</tag>".'
>>> import html
>>> print(s)
"<tag>text</tag>"
>>> print(html.escape(s))
"&quot;&lt;tag&gt;text&lt;/tag&gt;&quot"
# Disable escaping of quotes
>>> print(html.escape(s, quote=False))
"&lt;tag&gt;text&lt;/tag&gt"
```

> to process text in other direction, use the proper parser to fdo that 

```python
>>> s = 'Spicy &quot;Jalape&#241;o&quot.'
>>> from html.parser import HTMLParser
>>> p = HTMLParser()
>>> p.unescape(s)
'Spicy "Jalapeño".'
>>>
>>> t = 'The prompt is &gt;&gt;&gt;'
>>> from xml.sax.saxutils import unescape
>>> unescape(t)
'The prompt is >>>'
```

### Tokenizing text
> Very specific use. See chapter 2.18, 2.19. See also [PyParsing](http://pyparsing.wikispaces.com/) or [PLY](http://www.dabeaz.com/ply/ply.html) for more details. 



