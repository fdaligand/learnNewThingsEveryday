# learnNewThingsEveryday
List of things learned day by day 


# Code
## Design Pattern 
### Law of Demeter (LoD)
>LoD is a specific case of loose coupling.
>The motto is **"Only talk to your immediate friends"**.
>It can be summarized in following ways : 
> * Each unit should have only limited knowledge about other units: only units "closely" related to the current unit.
> * Each unit should only talk to its friends; don't talk to strangers
> * Only talk to your immediate friends.

 * date : 03/01/2017
 * media : Wikipédia

### Command pattern 
>Behavioral design pattern in which an object is used to encapsulate all information to perform an action or trigger an event at a later time.

 * date : 27/01/2017
 * media : Wikipédia
 * link : https://en.wikipedia.org/wiki/Command_pattern

## Head First Design Pattern 
### Design principle
 * Identify the aspects of your application that vary and separate them from what stays the same.
 * Program to an interface, not an implementation
 * Favor composition over inheritance

### Design Pattern
#### STRATEGY
>The Stategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independentely from clients tahat us it.


### Python 3
#### Core 
>sum-up : New Dictionaries implementation in Python 3.6
 
 * date : 30/12/2016
 * media : Youtube
 * author : Raymond Hettinger
 * link : https://youtu.be/p33CVV29OG8

#### To be investigated 
* Code smell
* Python abstract class
* aspect oriented programming
* Low coupling principle

## Web 

### Internal browser 
#### WebAssembly (wasm)
>WebAssembly is an emerging standard whose goal is to define a safe, portable, size- and load-time efficient binary compiler target which offers near-native performance—a virtual CPU for the Web.

* date 10/02/2017
* media : hachs mozilla 
* link 
    - [A WebAssembly Milestone: Experimental Support in Multiple Browsers](https://hacks.mozilla.org/2016/03/a-webassembly-milestone/)
## Tools

## Source control

### Git 
#### Git stash 
>Stash the change in a dirty working directory away

* date : 10/01/2017
* media : Git official doc 
* [link](https://git-scm.com/docs/git-stash)

#### Git tutorial 
>Learn interactively with web browser how to branch/merge/rebase/cherry-pick....

 * date : 19/01/2017
 * media : GitHub Page
 *  
#### To be investigated 
* Git fsck 
 
## Unix 

### Grep
* find file in directory which not include specific pattern 
    - `grep -Lr "string to find" *`
* check multiple extension 
    - ` grep -E '.h|.cpp'` or `grep -e '.h\|.cpp'`