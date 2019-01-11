
# CHAPITER 13 : Manipulating Text

## Cat

stand for *concatenate*.  
`cat readme.txt` will display the contents of readme.txt on the terminal.
The `tac` command (cat spelled backwards) prints the lines of a file in reverse order.

### Using cat interactively 
To create a new file, at the command prompt type `cat > <filename>` and press the **Enter** key (use `>>` to append at the end of file).

This command creates a new file and waits for the user to edit/enter the text. After you finish typing the required text, press <kbd>CTRL-D</kbd> at the beginning of the next line to save and exit the editing.

Another way to create a file at the terminal is `cat > <filename> << EOF`. A new file is created and you can type the required input. To exit, enter `EOF` at the beginning of a line.

**Note that EOF is case sensitive**. One can also use another word, such as `STOP`.

```sh
flo@flo-X301A:~/git/learnNewThingsEveryday$ cat > test_cat.txt
plip
plop
toto
tata
flo@flo-X301A:~/git/learnNewThingsEveryday$ cat test_cat.txt 
plip
plop
toto
tata
flo@flo-X301A:~/git/learnNewThingsEveryday$ 
```


## echo 

`echo` simply displays (echoes) text.  

The `–e` option, along with the following switches, is used to enable special character sequences, such as the newline character or horizontal tab.
 * `\n`  represents newline
 * `\t`  represents horizontal tab.

## less 

Use `less` to read large files 

## head

`head` reads the first few lines of each named file (10 by default) and displays it on standard output.

## tail 

`tail` prints the last few lines of each named file and displays it on standard output. By default, it displays the last 10 lines. 

To continually monitor new output in a growing log file:
```
$ tail -f somefile.log 
```
This command will continuously display any new lines of output in atmtrans.log as soon as they appear.  


## View Compressed files 

| Command | Description |
| --- | --- |
| $ zcat compressed-file.txt.gz | To view a compressed file |
| $ zless somefile.gz or $ zmore somefile.gz | To page through a compressed file |
| $ zgrep -i less somefile.gz | To search inside a compressed file |
| $ zdiff file1.txt.gz file2.txt.gz | To compare two compressed files |

There are also equivalent utility programs for other compression methods besides `gzip`, for example, we have `bzcat` and `bzless` associated with `bzip2`, and `xzcat` and `xzless` associated with xz.  

## sed 

Stream editor. 

![sed](img/sed.jpg)

`sed -e command <filename>` Specify editing commands at the command line, operate on file and put the output on standard out (e.g., the terminal).  
The -e command option allows you to specify multiple editing commands simultaneously at the command line. It is unnecessary if you only have one operation invoked.

`sed -f scriptfile <filename>` Specify a scriptfile containing sed commands, operate on file and put output on standard out