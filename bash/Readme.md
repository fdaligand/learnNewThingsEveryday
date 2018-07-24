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

### Compound commands 
End of page 9