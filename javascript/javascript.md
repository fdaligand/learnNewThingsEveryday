# Javascript learning 

## Type 

 * Number
 * String
 * Boolean
 * Symbol (new in ES2015)
 * Object
 * Function
    - Array
    - Date
    - RegExp
 * null
 * undefined

### `null` vs `undefined`

`null` : value that indicates a deliberate non-value.
`undefined` : indicate an uninitialized value.

### `true` and `false`

`false` : `false`,`0`,empty strings (`""`),`Nan`,`null`,`undefined`
`true` : all other value.

## Number
> Numbers in JavaScript are "double-precision 64-bit format IEEE 754 values". The standard arithmetic operators are supported. You can convert a string to an integer using the built-in `parseInt()`. Use *unary operator* to convert values to number.

```javascript
+ '42'; //42

parseInt('10.2abc')
>>10
parseFloat('10.2abc')
>>10.2
+"10.2abc"
>>NaN
```

### NaN
Means "not a number". Returned during conversion if string is non-numeric. `Nan` is toxic and will be propageted to result. Use `isNan()` for test.
```javascript
parseInt('hello', 10); // NaN
NaN + 5; // NaN
isNaN(NaN); // true
```

### Infinity
```javascript
1 / 0; //  Infinity
-1 / 0; // -Infinity
isFinite(1 / 0); // false
isFinite(-Infinity); // false
isFinite(NaN); // false
```

## Variable

New variables in JavaScript are declared using one of three keywords: `let`, `const`, or `var`. 

### let 
declare block level variable. 
```javascript
// myLetVariable is *not* visible out here

for (let myLetVariable = 0; myLetVariable < 5; myLetVariable++) {
  // myLetVariable is only visible in here
}

// myLetVariable is *not* visible out here
```

### const
decalre value wthat will are never intended to change. Available from the function block where it it declared.
```javascript
const Pi = 3.14; // variable Pi is set 
Pi = 1; // will throw an error because you cannot change a constant variable.
```

### var
Available from the function block it is declared in.
**An important difference between JavaScript and other languages like Java is that in JavaScript, blocks do not have scope; only functions have scope. So if a variable is defined using var in a compound statement (for example inside an if control structure), it will be visible to the entire function. However, starting with ECMAScript 2015, let and const declarations allow you to create block-scoped variables.**
Variable declared without assigning will be `undefined`

## Operator 
### `==`
perform type coercion if you give it different type.
```javascript
"toto" == "toto"
true
"toto" == "tata"
false
"toto" == 123
false
"123" == 123
true
```

### `===`
Avoid type coercion.
```javascript
"toto" === "toto"
true
"toto" === "tata"
false
"toto" === 123
false
"123" === 123
false
```

## Control structure

### for...of
The for...of statement creates a loop iterating over iterable objects (including `Array`, `Map`, `Set`, `String`, `TypedArray`, `arguments` object and so on), invoking a custom iteration hook with statements to be executed for the value of each distinct property.
```javascript
// String
let iterable = 'boo';

for (let value of iterable) {
  console.log(value);
}
// "b"
// "o"
// "o"

// TypeArray
let iterable = new Uint8Array([0x00, 0xff]);

for (let value of iterable) {
  console.log(value);
}
// 0
// 255
// Map
let iterable = new Map([['a', 1], ['b', 2], ['c', 3]]);

for (let entry of iterable) {
  console.log(entry);
}
// ['a', 1]
// ['b', 2]
// ['c', 3]

for (let [key, value] of iterable) {
  console.log(value);
}
// 1
// 2
// 3

// Argument
(function() {
  for (let argument of arguments) {
    console.log(argument);
  }
})(1, 2, 3);

// 1
// 2
// 3

// Generators
function* fibonacci() { // a generator function
  let [prev, curr] = [1, 1];
  while (true) {
    [prev, curr] = [curr, prev + curr];
    yield curr;
  }
}

for (let n of fibonacci()) {
  console.log(n);
  // truncate the sequence at 1000
  if (n >= 1000) {
    break;
  }
}
```

### for...in
The for...in statement iterates over the **enumerable properties** of an object, in original insertion order. For each distinct property, statements can be executed.
```javascript
var obj = {a: 1, b: 2, c: 3};
    
for (var prop in obj) {
  console.log('obj.' + prop, '=', obj[prop]);
}

// Output:
// "obj.a = 1"
// "obj.b = 2"
// "obj.c = 3"
```
inherited properties are not displayed
```javascript
var triangle = {a: 1, b: 2, c: 3};

function ColoredTriangle() {
  this.color = 'red';
}

ColoredTriangle.prototype = triangle;

var obj = new ColoredTriangle();

for (var prop in obj) {
  if (obj.hasOwnProperty(prop)) {
    console.log('obj.' + prop + ' = ' + obj[prop]);
  } 
}

// Output:
// "obj.color = red"
```

### `&&` and `||`
Use short-circuit logic, which means whether they will execute their second operand is dependent on the first. This is useful for checking for null objects before accessing their attributes.

### ternary operator `?:`
```javascript
var allowed = (age > 18) ? 'yes' : 'no';
```

## Objects
Objects are :
 * Dictionaries in Python
 * Hashes in Perl and Ruby
 * Hash tables in C and C++
 * HashMaps in Java
 * Associative arrays in PHP
There are two way to create an object : 
```javascript
var obj = new Object();
//or
var obj = {}; // object litteral syntax
```
Object literal syntax can be used to initialize an object 
```javascript
var obj = {
  name: 'Carrot',
  'for': 'Simon',
  details: {
    color: 'orange',
    size: 12
  }

obj.details.color; // orange
obj['details']['size']; // 12
obj.for = 'Simon'; // Syntax error, because 'for' is a reserved word
obj['for'] = 'Simon'; // works fine
}
```
See doc on [Inheritance and the prototype chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain)

## Array

## Ressources
 * [A re-introduction to JavaScript (JS tutorial)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript#Introduction)