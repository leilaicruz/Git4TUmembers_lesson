
Time estimation : 

Introduction: 10:00- 10:30
Lesson : 10:30-11:30
Break: 11:30-11:45
Lesson: 11:45-12:30

Lunch: 12:30 - 13:30

## Preparation in my terminal 

- Write

```bash
cd /mnt/c/Users/linigodelacruz/Desktop/
```
- Remove everything that is front '$' for a better view of commands:

```bash
export PS1='$ '
```

# Description of the shell before commands
The shell typically uses $ as the prompt, but may use a different symbol. In the examples for this lesson, we’ll show the prompt as $. Most importantly, do not type the prompt when typing commands. Only type the command that follows the prompt. This rule applies both in these lessons and in lessons from other sources. Also note that after you type a command, you have to press the Enter key to execute it.

# Listing content of your current folder 

```bash
ls
```

## Command not found

```bash
ks
```
 If the shell can’t find a program whose name is the command you typed, it will print an error message such as:

 ```bash
 command not found
 ```
This might happen if the command was mis-typed or if the program corresponding to that command is not installed.

## Current directory

```bash
pwd
```

## Home directory 

```bash
cd 
```

- Go to slides to show 


The home directory path will look different on different operating systems. On Linux, it may look like /home/nelle, and on Windows, it will be similar to C:\Documents and Settings\nelle or C:\Users\nelle. (Note that it may look slightly different for different versions of Windows.) 

The topmost directory is the root directory that holds everything else. We refer to it using a slash character, /, on its own; this character is the leading slash in /Users/nelle.

Inside that directory are several other directories: bin (which is where some built-in programs are stored), data (for miscellaneous data files), Users (where users’ personal directories are located), tmp (for temporary files that don’t need to be stored long-term), and so on.

## Listing with file properties 

```bash
ls --F
```

a trailing / indicates that this is a directory
@ indicates a link
* indicates an executable

## ask for help of each command

```bash
ls --help
pwd --help
cd --help 
```

### Exercise : 
https://swcarpentry.github.io/shell-novice/02-filedir.html#relative-path-resolution

Break : 15 mins

# Working with files and directories 

- Create a directory hierarchy that matches a given diagram.
- Delete, copy and move specified files and/or directories.

## Lets build a file structure as :
(Go to slides to visualize it)
Thesis
|── data/
│   |── a.dat
│   |── b.dat
│   |── c.dat
|── docs/
|── scripts/
      |── raw_data_processing.py
manuscript.tex

## Moving files and directories

- Change the name of the a.dat data file into a more informative name : optical_absorbance_600nm.dat 

```bash
mv data/a.dat data/optical_absorbance_600nm.dat
```
    - we just rename the a.dat file 

## Copying files 

```bash
cp manuscript.tex data/docs/manuscript.tex
```
- create a thesis backup 

```bash
cp -r Thesis Thesis-backup
```

## Removing files

```bash
rm manuscript.tex
```
- remove the folder Thesis and Thesis-backup 

```bash
rm -r Thesis Thesis-backup
```
