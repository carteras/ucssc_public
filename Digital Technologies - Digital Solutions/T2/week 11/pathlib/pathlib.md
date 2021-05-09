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
from pathlib import Path 
p = Path("C:/Users/carte/Desktop/github/ucssc/2021")
print(p)
```

### Constructing a path in parts

More often than not, we will want to do something that combines different parts of a path. 

Create a new python file called `paths3.py`

```python
from pathlib import Path 

p = Path("C:/Users/carte/Desktop/github/ucssc/2021")
print(p/'test.txt')
```

### Reading and Writing Files

Generally speaking the point of using a path is to access a file or database to read or write to. 

Pathlib has it's own open implementation so we connect our path object and open with dot syntax. 

reading a file
```python
from pathlib import Path

source_path = Path.cwd()
destination_path = source_path / "copy_to"
file_path = source_path / "test.txt"

if source_path.exists():
    with file_path.open(mode='r') as file_reader:
        for line in file_reader:
            print(line)
```

### Moving files

Using pathlib we can locate the two paths and then just write to each other
```python
from pathlib import Path

digital_tech_path = Path(r'Digital Technologies - Digital Solutions\T2\week 11\pathlib\test')
file_source = 'foo/'
file_name = 'animal.jpg'
file_path = digital_tech_path / file_source / file_name

destination = digital_tech_path / Path("temp/")

destination.mkdir(parents=True, exist_ok=True)
destination_file = destination / file_name

destination_file.write_bytes(file_path.read_bytes())
#destination_file.write_text(file_path.read_text())

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

To delete a file we use the unlink command. Unlink removes the file system pointer from the file allowing the operating system to remove it when there are available resources. If the path points to a directory, use Path.rmdir() instead.

```python
from pathlib import Path

digital_tech_path = Path(r'Digital Technologies - Digital Solutions\T2\week 11\pathlib\test')
file_source = 'foo/'
file_name = 'animal.jpg'
file_path = digital_tech_path / file_source / file_name

destination = digital_tech_path / Path("temp/")

destination.mkdir(parents=True, exist_ok=True)
destination_file = destination / file_name

destination_file.write_bytes(file_path.read_bytes())

destination_file.unlink()


```
### Making a new directory
To make a new directory we use the `mkdir` command. This is a replication of posix system commands. 

```python
from pathlib import Path
p = Path.cwd() /  "new_dir"
p.mkdir(parents=True, exist_ok = True)

```

### Listing files in a directory
```python
from pathlib import Path

digital_tech_path = Path(r'Digital Technologies - Digital Solutions\T2\week 11\pathlib\test')
file_source = 'foo/'
file_name = 'animal.jpg'
file_path = digital_tech_path / file_source / file_name

destination = digital_tech_path / Path("temp/")

destination.mkdir(parents=True, exist_ok=True)
destination_file = destination / file_name

destination_file.write_bytes(file_path.read_bytes())

# destination_file.unlink()

files = destination.glob('*\.')
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

