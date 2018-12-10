## Finding files 

* Specify the type 
`find / -type f -name toto.txt`
`find / -type d -name directory`

 * Based on time 
`$ find / -ctime 3`
* File accessed
`$ find / -atime 3`
* File modified
`$ find / -mtime 3`

`3` means `n 3` and represent more than 3 days. To represent other times, use :
 * `[+/-][cam]min` 

* Based on size 
`find / -size 0`
` find / -size +10M -exec command {} ';'` 

## Package management 
![Package manager](img/Package_Managers.png)


| Operation | RPM | deb | 
| --- | --- | --- |
| Install package | rpm -i foo.rpm | dpkg --install foo.deb |
| Install package, dependencies | yum install foo | apt-get install foo |
| Remove package | rpm -e foo.rpm | dpkg --remove foo.deb |
| Remove package, dependencies | yum remove foo | apt-get autoremove foo |
| Update package | rpm -U foo.rpm | dpkg --install foo.deb |
| Update package, dependencies | yum update foo | apt-get install foo |
| Update entire system | yum update | apt-get dist-upgrade  |
| Show all installed packages | rpm -qa yum list installed | dpkg --list |
| Get information on package | rpm -qil foo | dpkg --listfiles foo |
| Show packages named foo | yum list "foo" | apt-cache search foo |
| Show all available packages | yum list | apt-cache dumpavail foo |
| What package is file part of? | rpm -qf file | dpkg --search file |

## Summary 


            Virtual terminals (VT) in Linux are consoles, or command line terminals that use the connected monitor and keyboard.

            Different Linux distributions start and stop the graphical desktop in different ways.

            A terminal emulator program on the graphical desktop works by emulating a terminal within a window on the desktop.
            The Linux system allows you to either log in via text terminal or remotely via the console.

            When typing your password, nothing is printed to the terminal, not even a generic symbol to indicate that you typed.
            The preferred method to shut down or reboot the system is to use the shutdown command.

            There are two types of pathnames: absolute and relative.
            An absolute pathname begins with the root directory and follows the tree, branch by branch, until it reaches the desired directory or file.

            A relative pathname starts from the present working directory.
    Using hard and soft (symbolic) links is extremely useful in Linux.

            cd remembers where you were last, and lets you get back there with cd -.
    
            locate performs a database search to find all file names that match a given pattern.
    
            find locates files recursively from a given directory or set of directories.
    
            find is able to run commands on the files that it lists, when used with the -exec option.
    
            touch is used to set the access, change, and edit times of files, as well as to create empty files.
    
            The Advanced Packaging Tool (apt) package management system is used to manage installed software on Debian-based systems.
    
            You can use the Yellowdog Updater Modified (yum) open source command-line package management utility for RPM-compatible Linux operating systems.
    
            The zypper package management system is based on RPM and used for openSUSE.


