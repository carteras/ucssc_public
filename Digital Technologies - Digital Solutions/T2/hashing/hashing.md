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


