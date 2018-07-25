# Bash Reference Manual
> Bourne Against Shell, written by Stephane Bourne

## Basic Shell Features
### Shell Operation 
 1. Read the inputs
 2. Breack the input into worlds and operator 
 3. Parse the tokens into simple and coumpound commands
 4. Performs the various shell expansions 
 5. Perform any necessary redirections 
 6. Exec the command
 7. Optionally wait for the command

### Quoting 
> use to remove meaning of certain characters or words to the shell   

Escape Character (`\`) : preserve the litteral value f the next char 
Single quote  (`'`) : preserve the literal value of each char within the quotes.
Double quotes (`"`) : preserves the literal value of all characters within
the quotes, with the exception of ‘$’, ‘‘’, ‘\’, and, when history expansion is enabled, ‘!’.

### Pipelines 

> A pipeline is a sequence of one or more commands separated by one of the control operators
‘|’ or ‘|&’.

```shell
[time [-p]] [!] command1 [ | or |& command2 ] ...
```
`time` causes timing statistic 
If ‘|&’ is used, command1’s standard error, in addition to its standard output, is connected to command2’s standard input through the pipe.
 * `|& == 2>&1 |`

The exit status of a pipeline is the exit status of the last command in the pipeline, unless the `pipefail` option is enabled

### List of command

`&`: shell execute the command asynchronously in a subshell (in background). the standard input is redirected to `/dev/null`
`;`: execute command sequentially, wait for each command to terminate.  
`command1 && command2`:command2 is executed if, and only if, command1 returns an exit status of zero.  
`command1 || command2`: command2 is executed if, and only if, command1 returns a non-zero exit status.  

### Loopig construct 
*until*: `until test-commands; do consequent-commands; done`  
Execute consequent-commands as long as test-commands has an exit status
which is not zero.
*while*: `while test-commands; do consequent-commands; done`  
Execute consequent-commands as long as test-commands has an exit status
of zero.
*for*: `for name [ [in [words ...] ] ; ] do commands; done`  
Expand words, and execute commands once for each member in the resultant
list, with name bound to the current member.

`breack` and `contniue` can be use to control loop.

### Coniditional Constructs
*if*: `if test-commands; then
consequent-commands;
[elif more-test-commands; then
more-consequents;]
[else alternate-consequents;]
fi`  
*case*: `case word in [ [(] pattern [| pattern]...) command-list ;;]... esac`
set `nocasematch` to shell option (`shopt`) to ignore case on match.  
It’s a common idiom to use `*` as the final pattern to define the
default case
Each clause must be terminated with `;;`,`;&`, or `;;&`.
`;&` :causes execution to continue with the command-list associated with the next clause
`;;&`: causes the shell to test the patterns in the next clause, if any, and execute
any associated command-list on a successful match
