# Hashing

## You will learn how to create a hash from a string or file in python

## Using Hashlib 
The module that holds all of the hashing algorithms (that we are interested in) is in the `hashlib` module. To import it we can choose to import all of it with a single import statement: 

```python
import hashlib 
m = hashlib.md5()
```

or we can be more specific and only call the items we need. 

```python
from hashlib import md5
m = md5()
```
### using a hash algorithm

To use a hash algorithm we need to 
* update the message with content (in this case as a byte stream)
* read the converted digest message

```python
import hashlib 

m = hashlib.md5()
m.update(b"Nobody expects")
m.update(b"the Spanish inquisition")

print(m.digest())
```

### digest vs hexdigest

`.digest(data)` returns a byte object and contains string byte references. 
`.hexdigest(data)` returns a string object of double length only containing hexadecimal digits. This is the most common way we see digest data for hashs. 

```python
import hashlib 

m = hashlib.md5()
m.update(b"Nobody expects")
m.update(b"the Spanish inquisition")

print(m.hexdigest())
```

### hash.update(data)
Update the hash object with the bytes-like object. Repeated calls are equivalent to a single call with the concatenation of all the arguments: m.update(a); m.update(b) is equivalent to m.update(a+b).



## Using Hashes 

### encoding messages 

Instead of putting a `b` in front of strings we can also use the `'.encode(type)` command. They are interchangeable. 

```python
message = 'Nobody expects the spanish inquisition'
print(message)
print(message.encode('utf-8'))
```
```
Nobody expects the spanish inquisition
b'Nobody expects the spanish inquisition'
```


### make_hash function

```python
from hashlib import md5

def make_hash(pass_phrase):
    pass_phrase = pass_phrase.encode('utf-8')
    m = md5()
    m.update(pass_phrase)
    return m.hexdigest()

message = 'Nobody expects the spanish inquisition'
hashed_msg = make_hash(message)
print(message)
print(hashed_msg)
```

### Using make_hash with different algorithms

```python
from hashlib import md5, sha1

def make_hash(pass_phrase, algorithm='md5'):
    m = None
    if algorithm == 'md5':
        m = md5()
    elif algorithm == 'sha1':
        m = sha1()
    else:
        return -1
    pass_phrase = pass_phrase.encode('utf-8')
    m.update(pass_phrase)
    return m.hexdigest()

message = 'Nobody expects the spanish inquisition'
hashed_msg = make_hash(message, 'sha1')
print(message)
print(hashed_msg)
```

## Using Dictionaries to store hashes

```python
from hashlib import md5, sha1

passwords = [
    'password',
    'password!',
    'passw0rd'
]

def make_hash(pass_phrase, algorithm='md5'):
    m = None
    if algorithm == 'md5':
        m = md5()
    elif algorithm == 'sha1':
        m = sha1()
    else:
        return -1
    pass_phrase = pass_phrase.encode('utf-8')
    m.update(pass_phrase)
    return m.hexdigest()

password_hashes = {}

for password in passwords:
    password_hashes[password] = make_hash(password)

for key in password_hashes:
    print(f'{key}\t{password_hashes[key]}')
```
### Hashing files

Hashing files takes a little more work. Because it is a file, we need to read it like a file. Remembering to set the read permissions to read binary mode (because it's a file not a text document).

```python
from pathlib import Path
from hashlib import md5, sha256

def make_hash(file_path, algorithm='md5'):
    """ creates either MD5 or SHA256 hashes from files
    
    This function takes the file_path of a file and creates a hash. The hash is selected as md5 as default but can be switched to SHA256 by using the algorithm keyword argument. 

    Parameters:
    file_path: a pathlib path of the file to be hashed
    algorithm: the type of algorithm to use for hashing. 

    Returns:
    Either an MD5 hash or a SHA256 hash of the given file.     
    """

    # selects MD5 by default. (is this optimum?)
    out = md5() 

    # if algorithm was sha256, switch to that. 
    if algorithm == 'sha256':
        out = sha256()

    # opens a file in read binary mode as file_reader
    with open(file_path, 'rb') as file_reader:
        # read a chunk of data from the file and assign it to byte
        while (byte := file_reader.read(out.block_size)):
            # update out with the chunk of data. 
            out.update(byte) 

    # return the hash as a hexdigest. 
    return out.hexdigest()

# Setting the directory to where hash objects are. 
my_file_directory = Path().cwd() / "2021/Digital Technologies - Digital Solutions/T2/hashing"

# hand crafting my dictionary. 
hash_objects = {
    'plane': my_file_directory / 'plane.jpg',
    'ship' : my_file_directory / 'ship.jpg'
}


#making a fancy print of my hash files
for key in hash_objects:
    ho = hash_objects[key]                         # assigning a common variable name because I am lazy
    print(f'Directory: {ho.parent}')               # path_object.parent is the directory without the file name
    print(f'File name: {hash_objects[key].name}')  # path_object.name is the name and extension
    print(f'hash: {make_hash(hash_objects[key])}') # hashing file
```

## Challenges

### Basic Challenge 

Create a command line hashing program that can create a hash of a given file. Create optional parameters for at least 2 hashing programs including MD5. MD5 must be the default option. 

example execution code

`python hashing_challenge1.py file.foo`

Test both `plane.jpg` and `ship.jpg`. 

Your output must look like: 

```
plane.jpg       253dd04e87492e4fc3471de5e776bc3d
ship.jpg        253dd04e87492e4fc3471de5e776bc3d
````
NOTE: `Path('file_name').name` will return the file + extension
### Intermediate Challenge 1

Expanding the command line hashing program from above. Transform it so that it can read all of the files in a directory and then hash them and store those hashes. Test them against the images that are stored in the supplied zip file. 

example execution code: 

`python challenge2.py /dir/`

Your output would be similar to challenge1 except contain all of the files in the directory

### Advanced Challenge

Expanded the command line hashing program from above. Transform it so that if it detects a collision that you automatically test those two files with a different hashing algorithm. Create an optional parameter for this. `--detect_collisions`

The execution is the same as above. 

Output would be similar to challenge 1 but only files that had a collision


