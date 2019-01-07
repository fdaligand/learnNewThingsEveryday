# Chapter 11 Text Editor

create file using redirection 
```sh
$ cat << EOF > myfile
> line one
> line two
> line three
> EOF
$
```

## vi 

Use `vimtutor` to have a first tuto on vim.
`Vi` provides three modes :
 * **Command** : Each key is an editor command
 *  **Insert** : (Type i to switch to insert). Used to insert text in file, indicated by `? INSERT ?` in bootom of screen.
 *  **Line** : Type `:` from the command mode. Used to enter key as an external command.

### Basic command

| Command | Usage |
| --- | --- |
| :w myfile | Write out the file to myfile |
| :w! file2 | Overwrite file2 |
| :x or :wq | write file and quite |
| :q | quit |
| :q! | quit without saving |

In command mode : 
| command | Usage |
| j or <ret> | move line down |
| k | move line up |
| h | move one charactere left |
| h or Backspace | move char left |
| l or Space | move char right |
| 0 | move beginning of line |
| $ | move end of line |
| w | move beginning of next word |
| :0 or 1G | move to begiining of file |
| :n or nG | move to line n |
| :$ or G | move to end of file |
| CTRL-F or PAge Down | Move page forward | 
| CTRL-B or PAge Up | Move page forward | 
| ^l | refresh and center screen |
| /pattern | Search forward for pattern |
| ?pattern | Search backward for pattern |
| n | Move to next occurence of search pattern |
| N | Mov to previous occurence of search pattern |
| a (A) | append text after cursor (end of current line); Stop upon Escape Mode |
| i  | Insert text before cursor; Stop upon Escape Mode |
| I | Insert text at the beginning of current line |
| o (O) | Start a new line below (above) current line, insert text there |
| r | Replace char at current position |
| R | replace text starting with current position |
| x | delete char at current position |
| Nx | delete N char starting at current position |
| dw | delete word at current position |
| D | delete the rest of the current line |
| dd | delete the current line |
| Ndd or dNd | Delete N lines |
| u | undo teh previous operation |
| yy | Yank (copy) the current line and put it in buffer |
| Nyy| yNy | Yank N lines and put it in buffer |
| p | paste at the current position |


Typing `:sh` open an external command shell. When you exit the shell you return to vi opened file.
Typing `:!` executes a command from within vi. 
This technique is best suited for non-interactive commands, such as : ! wc %. Typing this will run the wc (word count) command on the file; the character % represents the file currently being edited.

## EMACS

Rather than having different modes for command and insert, like vi, emacs uses the `CTRL` and Meta (`Alt` or `Esc`) keys for special commands.
