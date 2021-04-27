# Using Python to navigate file structures using Pathlib

## You will learn

The concept for today is to use python to explore the filesystem. This is a critical tool as things like data sources are often held in directories away from code for safety reasons. 

## Pathlib 

Pathlib is fairly straight forward. 

### Creating a path object: Current Working Directory

The easiest way to create a path is to start from the common working directory. 

Path is an object within the path library. For out needs, a python object is kind of like a fancy function that holds data and functions. 

create a python file called `paths1.py`
```python 
import pathlib
p = pathlib.Path.cwd()
print(p)
```
```
> PS [your directory should appear here]
```

### Creating an explicit path from a string representation

Sometimes we need to reference something somewhere else and the easiest way to do this is with the string of that directory

NOTE: You will want to change your path to something that makes sense to you. Maybe h:/Programming or something

Create a python file called `paths2.py`
```python 
import pathlib
p = pathlib.Path("c:/Users/carte/Desktop/github/ucssc/2021\Digital Technologies - Digital Solutions/T2/week 11/pathlib/")
print(p)
```

### Constructing a path in parts

More often than not, we will want to do something that combines different parts of a path. 

Create a new python file called `paths3.py`

```python
import pathlib
digital_technologies_path = pathlib.Path.cwd()
week_11 = pathlib.Path('Week 11/')
pathlib_path = pathlib.Path('pathlib/')

all_together_now = digital_technologies_path / week_11 / pathlib_path
print('> ', all_together_now)
```

### Reading and Writing Files

Generally speaking the point of using a path is to access a file or database to read or write to. 

Pathlib has it's own open implementation so we connect our path object and open with dot syntax. 

```python
from pathlib import Path

digital_technologies_path = Path("Digital Technologies - Digital Solutions/T2/week 11/pathlib/test/")

print('-'*50)
with open(digital_technologies_path / 'foo.txt' , 'r') as fr:
    for line in fr:
        line = line.strip()
        print(line)
```

### Moving files

This is a hacky way of handling the moving of files. The best way of handling this is to 

Create 
```python
import pathlib
file_name = source / "text.txt"
if not destination.exists():
    with destination.open(file_name, 'w') as file_writer:
        for line in file_writer:
            file_writer.write(line)
```

easier way: 

```python
import pathlib
import shutil

my_file = pathlib.Path.cwd() / "test.txt"
to_file = pathlib.Path('/foo')

shutil.copy(my_file, to_file)
```

### Deleting files
```python
from pathlib import Path
folder = Path.cwd() / "foo/"
folder.rmdir()
file_name = Path.cwd() / "test.txt"
file_name.unlink()

```
### Making a new directory

```python
from pathlib import Path
p = Path.cwd() /  "new_dir"
p.mkdir(parents=True, exist_ok = True)

```

### Listing files in a directory
```python
from pathlib import Path 

files = Path.cwd().glob('*\.')
for f in files:
    if f.is_file():
        print(f)
```

### Picking out components of a path
```python
path = pathlib.Path.cwd()
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
print(path.parent.parent)
print(path.anchor)
```


*    .name: the file name without any directory
*    .parent: the directory containing the file, or the parent directory if path is a directory
*    .stem: the file name without the suffix
*    .suffix: the file extension
*    .anchor: the part of the path before the directories


## Challenges

### Basic Challenge1

Using the challenge.zip use the `challenge1.py` file to create a program that can list the files in the files directory. 

### Basic Challenge2

Extend this program to attempt to copy the files from the files directory to a new directory called files_out

