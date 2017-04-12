# Ruby most important fact 
## Object 
To find tyep of and object, ask for the `class` attribute of this object.
```ruby
[2] pry(main)> x = "hello world"
=> "hello world"
[3] pry(main)> x.class
=> String
```

## Array 

 * Array.push() : append to the end 
 * Array.pop() : remove to the end and return value
 * Array.unshift() : append to start
 * Array.shift() : remove to start and return value

append to array : `<<`

```ruby
array = [:peanut, :butter, :and, :jelly]
array[4,0] = []
array[5,0] = nil
```

```ruby
first_name, *last_name = ["John", "Smith", "III"]
first_name = "John"
last_name = [""]
```
`first_name, = ["John", "Smith"] => first_name = "John"`

#### test empty array 
```ruby 
    x = []
    x.any? => return false
    x.empty? => return true
```

#### find element in array 
```ruby
x = { :a => 2,:b => 2, c:= 3}
x.all? {|x| x < 3} => return false
x.any? {|x| x < 3} => return true
```

## Range

`(1..5) != [1,2,3,4,5]`

`(1..5).to_a == [1,2,3,4,5]`

`(1...5).to_a == [1,2,3,4]`

## Hash

* `Hash.new("toto")` => "toto" will be used as default value 
```ruby
irb(main):001:0> x = Hash.new("toto")
=> {}
irb(main):002:0> x[:a] = 10
=> 10
irb(main):003:0> x
=> {:a=>10}
irb(main):004:0> x[10]
=> "toto"
irb(main):005:0> x["10"]
=> "toto"
```
* hash.fetch(key) : retrun the mentionned key. If key doesn't exist, raise an error (KeyError)# 
* hash[key] : retrun the mentionned key. **nil object if key doesn't exist**
* hash key is not string but symbols
* hash.merge(hash) : merge to hash together

## Strings
* Use flexible quoting ( `%()` or `%!!` or `%{}`) for complexe string ( mix in `'` and `"`, multi lines)
* plus equals operator `+=` will not modify string
```ruby
original_string = "Hello, "
hi = original_string
there = "World"
hi += there
assert_equal "Hello, ", original_string
```
* shovel operator `<<` modify string 
```ruby
original_string = "Hello, "
hi = original_string
there = "World"
hi << there
assert_equal "Hello, World", original_string
```
* `""` automaticaly interpret escape characteres conversely `''`
* use `#{}`,**in double quote (`""`)**, to interpolate variable in string , or to call function. **Single quote (`''`) don't interpolate value**
```ruby
string = "Bacon, lettuce and tomato"
string[7,3] #print 'let'
string[7..9] #print 'let'

a = "a string"
b = "a string"

assert_equal true, a           == b
assert_equal false, a.object_id == b.object_id
```
Use `include?` to find substring in string.
```ruby
[18] pry(main)> x = "hello world"
=> "hello world"
[19] pry(main)> x.include? "world"
=> true
[20] pry(main)> x.include? "word"
=> false
```

## Symbols
```ruby
symbol = :ruby
symbol.is_a?(Symbol) # true
```

* Counter to `string`, to `symbol` decalaration with the same value have the same `object_id`.
* Variable name starting with a capital letter become a constant. Constant can be assigned only once and raise warning if new assignement is tried. Ruby automatically convert constant to symbols
```ruby
RubyConstant = " declare a string as constant"
Symbol.all_symbols.include?(:RubyConstant)
=> true
```
* To convert `String` to `Symbols`, use `String.to_sym`. **Space are tolered to create symbols**
* `Symbols` is not equal to `String`, and do not have its method
* `Symbols` can't be concatenated  

## Regexp

```ruby
=>"toto tata titi"[/tata/]
=> "tata"
=> "toto tata titi"[/tete/]
=> nil
```
* `?` : 0 or 1
* `+` : 1 or more
* `*` : zero or more
* the left most match wins
* use `/\d/` to search for a number (`[0-9]`)
* use `\s` to serach for whitespace charactere (`[ \t\r\n\f]`)
* use `\w` to search for a word (`[a-zA-Z0-9_]`)
* use `.` to search for non-newline character 
* use `/[^]/` to make a negated search
* use `\D` to search for non-digit character (`[^0-9]`)
* use `\S` to search for non-whitespace character (`[^ \t\r\n\f]`)
* use `\W` to search for a word (`[^a-zA-Z0-9_]`)
* `\A` - Matches beginning of string.
* `\z` - Matches end of string.
* `^` - Matches beginning of line 
```ruby
    assert_equal "2", "num 42\n2 lines"[/^\d+/]
```
* `$` - Matches end of line
```ruby
    assert_equal "42", "2 lines\nnum 42"[/\d+$/]
```
* `\b` - Matches word boundaries when outside brackets; backspace (0x08) when inside brackets
* use bracket `()` to group contents
```ruby
    assert_equal "hahaha", "ahahaha"[/(ha)+/]
```
* also capture matched by content by specifying order or with prefix `$`
```ruby
    assert_equal "Gray", "Gray, James"[/(\w+), (\w+)/, 1]
    assert_equal "James", "Gray, James"[/(\w+), (\w+)/, 2]
    assert_equal "Gray, James", "Name:  Gray, James"[/(\w+), (\w+)/]
    assert_equal "Gray", $1
    assert_equal "James", $2
```
* Vertical pipe `|` means or
* use `scan(/pattern/)` to find all occurence in a string. This method return an array.
* use `sub` to replace first occurence of a pattern or `gsub` to repalce all occurence.
```ruby
    assert_equal "one t-three", "one two-three".sub(/(t\w*)/) { $1[0, 1] }
    assert_equal "one t-t", "one two-three".gsub(/(t\w*)/) { $1[0, 1] }
```
---
---
---

## Ruby install. 
### gem 
package manager to easely install RubyGems ( as npm in javascript or pip in python)

### [Bundle](http://bundler.io/)

>Bundler provides a consistent environment for Ruby projects by tracking and installing the exact gems and versions that are needed. 

### Issue on SSL connection 
Sometimes error occurs on ssl connection 
```
> bundle install                                                                   
Fetching gem metadata from https://rubygems.org/..............                     
Fetching version metadata from https://rubygems.org/.                              
Resolving dependencies...                                                          
Using bundler 1.13.2                                                               
Gem::RemoteFetcher::FetchError: SSL_connect returned=1 errno=0 state=SSLv3 read    
server certificate B: certificate verify failed                                    
(https://rubygems.org/gems/concurrent-ruby-1.0.2.gem)                              
An error occurred while installing concurrent-ruby (1.0.2), and                    
Bundler cannot continue.                                                           
Make sure that `gem install concurrent-ruby -v '1.0.2'` succeeds before            
bundling.                                                                      
```
#### Workaround 
 Udpate (or add ) `sll_verify_mode` to `0` in the `.gemrc` of your home path. 
## Abort
Terminate execution immediately, effectively by calling `Kernel.exit(1)`.