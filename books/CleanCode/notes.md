# Clean code

> Robert C. Martin
Lean methods apply to code.

*Small things matter*, *God is in the details*  
In software, 80% or more of what we do is quaintly called
“maintenance”: the act of repair.  
In sotftware, focus on maintenance before on production.
5s:
 * *Seiri* (sort, organisation) => suitable naming  
 * *Seiton* (systematize) => code should be at palce that we expect to be
 * *Seiso* (shine, clean) => sanitize your code (no boller plate comments, ...)
 * *Seiketsu* (standardization) => how to get the workplace clean
 * *Shutsuke* (self-disciplien) => disciplien to follow the practice

Making your code readable is as important as making it executable.  
You should name a variable using the same care with which you
name a first-born child.  


## Introduction
crafsmanships : knowledges and **work** (practice).  
Learning to write clean code is hard work.  

## 1. Clean code
**Later equals never**  
Manager defend schedule and requirements with passion, we must defend the code with equal passion.  
It is unprofessional for programmers to bend to the will of managers who don’t
understand the risks of making messes.  
The only way to make the deadline—the only way to
go fast—is to keep the code as clean as possible at all times.  

The next time you write a line of code, remember you are an author,
writing for readers who will judge your effort.  
**making it
easy to read actually makes it easier to write.**  

Use the **Boy Scout Rule**: Leave the campground cleaner than you found it.

## 2. Meaningful Names
**Use Intention-Revealing Names** : The name of a variable, function, or class, should answer all the big questions. It
should tell you why it exists, what it does, and how it is used.  
**Avoid Disinformation**
**Make Meaningful Distinctions**: If names must be different, then they should also mean something different. Distinguish names in such a way that the reader knows what the differences offer.  
**Use Pronounceable Names**  
**Use Searchable Names**  The length of a name should correspond to the size of its scope.
**Avoid encodings**  
**Avoid Mental Mapping** 
Smart people sometimes like to show
off their smarts by demonstrating their mental juggling abilities. One difference between a smart programmer and a professional programmer is that
the professional understands that clarity is king. Professionals use their powers for good and write code that others can understand.  
**Class Names** : A class name should not be a verb  
**Method Names**: Methods should have verb or verb phrase.  
**Don’t Be Cute**: Choose clarity over entertainment value. Say what you mean. Mean what you say.  
**Pick One Word per Concept** : Pick one word for one abstract concept and stick with it. For instance, it’s confusing to have fetch , retrieve, and get as equivalent methods of different classes.  
**Use Solution Domain Names**: use
computer science (CS) terms, algorithm names, pattern names, math terms, and so forth.  
**Add Meaningful Context**
**Don’t Add Gratuitous Context** : Shorter names are generally better than longer ones, so long as they are clear. Add no more context to a name than is necessary.

## 3. Functions 
**Small!!!** : The first rule of functions is that they should be small. The second rule of functions is that
they should be smaller than that. 20 lines is the max admissible lenght.   
**Do one Thing** : Indent level should note be greater that, one or two.  
**FUNCTIONS SHOULD DO ONE THING. THEY SHOULD DO IT WELL. THEY SHOULD DO IT ONLY.**  
**One Level of Abstraction per Function**  
**Use Descriptive Names**  
> The ideal number of arguments for a function is
zero (niladic). Next comes one (monadic), followed
closely by two (dyadic). Three arguments (triadic)
should be avoided where possible. More than three
(polyadic) requires very special justification—and
then shouldn’t be used anyway.  

**Don't use Flag argument**:Flag arguments are ugly. Passing a boolean into a function is a truly terrible practice. It
immediately complicates the signature of the method, loudly proclaiming that this function
does more than one thing. It does one thing if the flag is true and another if the flag is false!  
**Output arguments**:  In general output arguments should be avoided. If your function must change the state
of something, have it change the state of its owning object.  
**Command Query Separation**: unctions should either do something or answer something, but not both.  
**Prefer Exceptions to Returning Error Codes** 
**Extract Try/Catch Blocks**  
**Error Handling Is One Thing**: a function using a try/catch should do only this things.  
**Don’t Repeat Yourself(DRY)**: Duplication may be the root of all evil in software.  

## 4. Comments
> **Don’t comment bad code—rewrite it.**

> Comments are always failures. We must
have them because we cannot always figure out how to express ourselves without them,
but their use is not a cause for celebration. 

> Truth can only be found in one place: the code.

> **Don’t Use a Comment When You Can Use a Function or a Variable**

**Comments Do Not Make Up for Bad Code** : Clear and expressive code with few comments is far superior to cluttered and complex
code with lots of comments.  
### Good comment 
 * legale comment (CopyRight, Licences, ...)
 * Informative Comments 
 * Explanation of intent 
 * Clarifications 
 * Warning of consequences
 * Todo 
 * Amplification
 
### Bad Comments
 * Mumbling : Comme,nt by habit or process
 * Redundant comments 
 * Misleading Comments : comments
that isn’t precise enough to be accurate
 * Mandated Comments
 * Journal Comments
 * Noise Comments : They restate the obvious and
provide no new information. 
 * Scary Noise
 * Position Markers
 * Closing Brace Comments : ```} // catch```
 * Attributions and Bylines : `/* Added by Rick */`
 * Commented-Out Code
 * HTML Comments
 * Nonlocal Information : describe the code that appear near, not systemwide info 
 * Too Much Information
 * Inobvious Connection : The connection between a comment and the code it describes should be obvious.
 * Function Headers : Short functions don’t need much description. A well-chosen name for a small function that
does one thing is usually better than a comment header.
 
## 5. Formatting
  
> If you are working on a team, then the team should agree to a single set of
formatting rules and all members should comply.

> Your style and discipline survives, even though your code does not.

> Small files are usually easier to understand than large files are.
### The Newspaper Metaphor
We would like a source file to be like a newspaper article.  
The name should be simple but explanatory.  
The topmost parts of the source file should provide the high-level concepts and algorithms.
Detail should increase as we move downward, until at the end we find the lowest level functions and details in the source file.  

> Concepts that are closely related should be kept vertically close to each other
Vertical Openness Between Concepts

Key Concepts:

* Vertical Openness Between Concepts
* Vertical Density : lines of code that are tightly related  should appear vertically dense.
* Vertical distance : Concepts that are closely related should be kept vertically close to each other
* Variable Declarations : Variables should be declared as close to their usage as possi-
ble.
* Instance variables:should be declared at the top of the class.
* Dependent Functions: If one function calls another, they should be vertically close,
and the caller should be above the callee, if at all possible.
* Vertical Ordering: In general we want function call dependencies to point in the downward direction. That is,
a function that is called should be below a function that does the calling 

## 6. Objects and Data Structures

>Serious thought needs
to be put into the best way to represent the data that an object contains. The worst option is
to blithely add getters and setters.  
> Objects hide
their data behind abstractions and expose functions that operate on that data. Data struc-
ture expose their data and have no meaningful functions.

__The law of demeter__ (talk to friend, not ot stranger) 

## 7. Error handling

* Use Exceptions Rather Than Return Codes
* Write Your Try-Catch-Finally Statement First
    - it is good practice to
start with a try - catch - finally statement when you are writing code that could throw
exceptions.
    - Try to write tests that force exceptions, and then add behavior to your handler to sat-
isfy your tests. This will cause you to build the transaction scope of the try block first and
will help you maintain the transaction nature of that scope.
* Provide Context with Exceptions
* Don't return Null : If you are tempted to return null from
a method, consider throwing an exception or returning a S PECIAL C ASE object instead.  
* Don't pass Null

## 8. Boundaries

### Vocabulaire 

* painstackingly = laborieusement 
* seldom = rarement 
* impediments (obstacle, barrier)
* colloquialisms (familliar)
* pun = jeux de mots 
* neatness = cleanness, cleanliness
### Go Further 
 * Agile Software Development: Principles, Patterns, and Practices (PPP)
