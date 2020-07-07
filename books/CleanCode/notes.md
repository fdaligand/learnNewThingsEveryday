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
page 53





### Vocabulaire 

* painstackingly = laborieusement 
* seldom = rarement 
* impediments (obstacle, barrier)
* colloquialisms (familliar)
* pun = jeux de mots 

### Go Further 
 * Agile Software Development: Principles, Patterns, and Practices (PPP)
