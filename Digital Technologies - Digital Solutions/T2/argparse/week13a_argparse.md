https://docs.python.org/3/howto/argparse.html

# Parsing arguments from the command line

## You will learn

## Argparse tutorial 



### Concept
What are command line arguments and why do we care? 

In this example we will use `ls`(list). The ls command (short for list) will show a directory-listing. It is one of the most common ones used when interacting with a text interface to a Linux system. It is the UNIX equivalent to the `dir` command common to many operating systems such as MS-DOS.

In this example, we use `ls` alone and it does the default action which is unlikely to break anything. 

```nginx
$ ls
cpython  devguide  prog.py  pypy  rm-unused-function.patch
```
This shows us a list of files and directories. 

But what happens if we want to list the contents of a subdirectory such as pypy? We can specify. 

```nginx
$ ls pypy
ctypes_configure  demo  dotviewer  include  lib_pypy  lib-python ...
```

When using `ls pypy` we tell the command line to list what is in the directory pypy. 

What about if we want to know more about the stuff we are listing? We can use `ls -l` to list in long form. The long option, `-l`, lists filenames, sizes, permissions, and other information.

```nginx
$ ls -l
total 20
drwxr-xr-x 19 wena wena 4096 Feb 18 18:51 cpython
drwxr-xr-x  4 wena wena 4096 Feb  8 12:04 devguide
-rwxr-xr-x  1 wena wena  535 Feb 19 00:05 prog.py
drwxr-xr-x 14 wena wena 4096 Feb  7 00:59 pypy
-rw-r--r--  1 wena wena  741 Feb 18 01:01 rm-unused-function.patch
```

What if we don't know anything about this command? We can ask it for help with `ls --help`
```nginx
$ ls --help
Usage: ls [OPTION]... [FILE]...
List information about the FILEs (the current directory by default).
Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.
...
```
### The Basics

Create a python program called `week_13a_1.py` and enter the following code

```python
from argparse import ArgumentParser

parser = ArgumentParser()
parser.parse_args() 
```
Open a terminal in VSC and navigate to the directory that you saved it. Use `ls` to find where you are starting, and then `cd directory` for each step. For example, I had to do 
```nginx
ls
cd '.\2021\Digital Technologies - Digital Solutions\'
ls
cd T2
ls
cd argparse
```
Make sure you have saved `week_13a_1.py` and in your terminal window type the following: 

```nginx
python .\week13a_argparse.py
python .\week13a_argparse.py foo
python .\week13a_argparse.py --verbose
python .\week13a_argparse.py -h 
```
Here's what I got. 

```nginx
PS D:\github\ucssc\2021\Digital Technologies - Digital Solutions\T2\argparse> python .\week13a_argparse.py                                                                                 
PS D:\github\ucssc\2021\Digital Technologies - Digital Solutions\T2\argparse> python .\week13a_argparse.py foo
usage: week13a_argparse.py [-h]
week13a_argparse.py: error: unrecognized arguments: foo
PS D:\github\ucssc\2021\Digital Technologies - Digital Solutions\T2\argparse> python .\week13a_argparse.py --verbose
usage: week13a_argparse.py [-h]
week13a_argparse.py: error: unrecognized arguments: --verbose
PS D:\github\ucssc\2021\Digital Technologies - Digital Solutions\T2\argparse> python .\week13a_argparse.py -h       
usage: week13a_argparse.py [-h]

optional arguments:
  -h, --help  show this help message and exit
PS D:\github\ucssc\2021\Digital Technologies - Digital Solutions\T2\argparse> 
```



### Positional arguments

Example code: 

```python
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('echo')
args = parser.parse_args()
print(args.echo)
```

Now run it. Here's what I got

```nginx
PS D:\github\ucssc\2021\Digital Technologies - Digital Solutions\T2\argparse> python .\week13a_argparse.py   
usage: week13a_argparse.py [-h] echo
week13a_argparse.py: error: the following arguments are required: echo
PS D:\github\ucssc\2021\Digital Technologies - Digital Solutions\T2\argparse>
```

We’ve added the add_argument() method, which is what we use to specify which command-line options the program is willing to accept. In this case, I’ve named it echo so that it’s in line with its function.

Calling our program now requires us to specify an option.

The parse_args() method actually returns some data from the options specified, in this case, echo.

The variable is some form of ‘magic’ that argparse performs for free (i.e. no need to specify which variable that value is stored in). You will also notice that its name matches the string argument given to the method, echo.

Note however that, although the help display looks nice and all, it currently is not as helpful as it can be. For example we see that we got echo as a positional argument, but we don’t know what it does, other than by guessing or by reading the source code. So, let’s make it a bit more useful:

```python
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('echo', help='Echos the string you use')
args = parser.parse_args()
print(args.echo)
```
```nginx
PS D:\github\ucssc\2021\Digital Technologies - Digital Solutions\T2\argparse> python .\week13a_argparse.py -h
usage: week13a_argparse.py [-h] echo

positional arguments:
  echo        Echos the string you use

optional arguments:
  -h, --help  show this help message and exit
PS D:\github\ucssc\2021\Digital Technologies - Digital Solutions\T2\argparse> 
```

Let's use it! 

```nginx
PS D:\github\ucssc\2021\Digital Technologies - Digital Solutions\T2\argparse> python .\week13a_argparse.py "the quick red fox jumped over the lazy hound"
the quick red fox jumped over the lazy hound
```

Let's make something a bit more useful

```python
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('square', help='squares a number')
args = parser.parse_args()
print(args.square**2)
```
Now run it! 
```nginx
PS D:\github\ucssc\2021\Digital Technologies - Digital Solutions\T2\argparse> python .\week13a_argparse.py 2
Traceback (most recent call last):
  File "D:\github\ucssc\2021\Digital Technologies - Digital Solutions\T2\argparse\week13a_argparse.py", line 6, in <module>
    print(args.square**2)
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int
```

That didn’t go so well. That’s because argparse treats the options we give it as strings, unless we tell it otherwise. So, let’s tell argparse to treat that input as an integer:

```python
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('square', help='squares a number', type=int)
args = parser.parse_args()
print(args.square**2)
```

### Introducing Optional arguments

So far we have been playing with positional arguments. Let us have a look on how to add optional ones:

```python
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--verbosity", help="increase output verbosity")
args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on")
else:
    print('verbosity was not turned on')
```
Now run it

```nginx
PS D:\github\ucssc\2021\Digital Technologies - Digital Solutions\T2\argparse> python .\week13a_argparse.py
verbosity was not turned on
PS D:\github\ucssc\2021\Digital Technologies - Digital Solutions\T2\argparse> python .\week13a_argparse.py --verbosity VERBOSITY  
verbosity turned on
PS D:\github\ucssc\2021\Digital Technologies - Digital Solutions\T2\argparse> python .\week13a_argparse.py --verbosity False      
verbosity turned on
PS D:\github\ucssc\2021\Digital Technologies - Digital Solutions\T2\argparse> python .\week13a_argparse.py --verbosity
usage: week13a_argparse.py [-h] [--verbosity VERBOSITY]
week13a_argparse.py: error: argument --verbosity: expected one argument
PS D:\github\ucssc\2021\Digital Technologies - Digital Solutions\T2\argparse>
```
Here is what is happening:

The program is written so as to display something when --verbosity is specified and display nothing when not.

To show that the option is actually optional, there is no error when running the program without it. Note that by default, if an optional argument isn’t used, the relevant variable, in this case args.verbosity, is given None as a value, which is the reason it fails the truth test of the if statement.

The help message is a bit different.

When using the --verbosity option, one must also specify some value, any value.

The above example accepts arbitrary integer values for --verbosity, but for our simple program, only two values are actually useful, True or False. Let’s modify the code accordingly:

```nginx
PS D:\github\ucssc\2021\Digital Technologies - Digital Solutions\T2\argparse> python .\week13a_argparse.py --verbosity 
verbosity turned on
PS D:\github\ucssc\2021\Digital Technologies - Digital Solutions\T2\argparse> python .\week13a_argparse.py --verbosity 1
usage: week13a_argparse.py [-h] [--verbosity]
week13a_argparse.py: error: unrecognized arguments: 1
PS D:\github\ucssc\2021\Digital Technologies - Digital Solutions\T2\argparse> python .\week13a_argparse.py --verbosity --help
usage: week13a_argparse.py [-h] [--verbosity]

optional arguments:
  -h, --help   show this help message and exit
  --verbosity  increase output verbosity
```

### Short Options
If you are familiar with command line usage, you will notice that I haven’t yet touched on the topic of short versions of the options. It’s quite simple:

```python
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-v", "--verbosity", help="increase output verbosity", action="store_true")
args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on")
else:
    print('verbosity was not turned on')
```

```nginx
PS D:\github\ucssc\2021\Digital Technologies - Digital Solutions\T2\argparse> python .\week13a_argparse.py --verbosity --help
usage: week13a_argparse.py [-h] [--verbosity]

optional arguments:
  -h, --help   show this help message and exit
  --verbosity  increase output verbosity
PS D:\github\ucssc\2021\Digital Technologies - Digital Solutions\T2\argparse> 
```

### Combining Positional and Optional Arguments 

```python
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('square', type='int', help="display a square of a given number")
parser.add_argument("-v", "--verbosity", help="increase output verbosity", action="store_true")
args = parser.parse_args()
if args.verbosity:
    print(f"The square of {args.square} equals {args.square**2}")
else:
    print(args.square**2)
```

```nginx
PS D:\github\ucssc\2021\Digital Technologies - Digital Solutions\T2\argparse> python .\week13a_argparse.py  
usage: week13a_argparse.py [-h] [-v] square
week13a_argparse.py: error: the following arguments are required: square
PS D:\github\ucssc\2021\Digital Technologies - Digital Solutions\T2\argparse> python .\week13a_argparse.py 2
4
PS D:\github\ucssc\2021\Digital Technologies - Digital Solutions\T2\argparse> python .\week13a_argparse.py 2 -v
The square of 2 equals 4
PS D:\github\ucssc\2021\Digital Technologies - Digital Solutions\T2\argparse> 
```

## Challenges

### Intermediate Challenges

* Accept a string and capitalize it depending on optional flags, --upper, --lower, --capitalize, --title.
* * Must accept both long and short optional commands
* * default scenario is to turn it to lower case
* * add a `--verbose` command that changes the output to "<input string> -> [MODIFIED|UNMODIFIED:] <output string>"

### Advanced Challenges

* * if in all scenarios if the string is already in that case add "UNMODIFIED: " to the start of the string
* * if modified add: "MODIFIED: " to the start of  the string