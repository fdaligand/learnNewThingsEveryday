# Chapter 8 Doc in Linux

## Man

`man –f` generates the same result as typing `whatis`.

`man –k` generates the same result as typing `apropos`.

The default order is specified in `/etc/man_db.conf` and is roughly (but not exactly) in ascending numerical order by section.

With the `-a` parameter, man will display all pages with the given name in all chapters, one after the other

## GNUinfo 

Typing `info` with no arguments in a terminal window displays an index of available topics. You can browse through the topic list using the regular movement keys: arrows, Page Up, and Page Down.

You can view help for a particular topic by typing `info <topic name>`. The  system then searches for the topic in all available info files.

## Graphical Help Systems

Type `yelp`

to read a man page in graphical interface type `yelp man:<command>`

## Package documentation 

read files on ` /usr/share/doc `

