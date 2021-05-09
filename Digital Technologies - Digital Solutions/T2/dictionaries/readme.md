## Python Programming: Dictionaries

A dictionary is a key-pair collection which is ordered by when the elements are inserted. 

You might be thinking to yourself "wait ... what?".  Imagine an actual dictionary. You look up a word (the key) and find the definition (the value). 

```
awesome adjective

awe·​some | \ ˈȯ-səm  \
Definition of awesome
1. inspiring awe
    * an awesome task/responsibility
    * a place of awesome beauty
    * binformal : TERRIFIC, EXTRAORDINARY
    * had an awesome time at the concert
2. expressive of awe
    * awesome tribute
```

### A simple dictionary
```python
#short and sharp
foo = {'key' : 'value'}

#if you have a lot of elements
bar = {
  'key1' : "value1",
  'key2' : 'value2'
}

print(foo['key'])
print(bar['key2'])

```

As written above a dictionary in python is a collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value that it is associated with. 

Keys are generally strings or maybe numbers. In general, the best practice is to make them identifiable to increase readability, i.e., strings. 

Values can be anything, numbers, strings, objects, lists, or even other dictionaries. 

### Working with dictionaries

To get a value from a key, simply give the name of the dictionary and the name of the key inside a set of square brackets. 

```python
adam = {'hair': 'ginger'}

print(adam['hair'])
```

You can have a practically unlimited number of key-value pairs. For example: 

```python
adam = {
  'hair':'ginger',
  'eyes':'hazel',
  'height':'tall',
  'profession':'nerdwrangler',
  'given_name':'adam'
}

print('Teachers, what is your profession!')
print(f"{adam['given_name']}: is a {adam['profession']}")
```

### Adding new key-value pairs

Dictionaries are dynamic in nature. This means that you can add new key-value pairs at any time. 

```python
adam = {
  'hair':'ginger',
  'eyes':'hazel',
  'height':'tall',
  'profession':'nerdwrangler',
  'given_name':'adam'
}

print(adam)
adam['family_name'] = 'carter
print(adam)
```

### Modifying a value 
The values of a dictionary are also dynamic. 
```python
adam = {
  'hair':'ginger',
  'eyes':'hazel',
  'height':'tall',
  'profession':'nerdwrangler',
  'given_name':'adam'
}
print(adam['hair'])
adam['hair'] = 'ginger striped with silver'
print(adam['hair'])
```

### Removing a key-value pair
Like lists, we can remove a key-value pair with the `del` command
```python
adam = {
  'hair':'ginger',
  'eyes':'hazel',
  'height':'tall',
  'profession':'nerdwrangler',
  'given_name':'adam'
}

for key in adam:
  print(key, adam[key])
```
### Iterating through a dictionary

```python
adam = {
  'hair':'ginger',
  'eyes':'hazel',
  'height':'tall',
  'profession':'nerdwrangler',
  'given_name':'adam'
}

for key in adam:
  print(f'This is the key {key}, and with it I can get the value {adam[key]}')
```

### Looping through all values in a dictionary

```python
adam = {
  'hair':'ginger',
  'eyes':'hazel',
  'height':'tall',
  'profession':'nerdwrangler',
  'given_name':'adam'
}

for feature in adam.values():
    print(feature)
```

### Data structures in Dictionaries
```python
people = {}
people['adam'] = {
    'hair':'ginger',
    'eyes':'hazel',
    'height':'tall',
    'profession':'nerdwrangler',
    'given_name':'adam'
}
people['ada'] = {
    'hair':'brown',
    'eyes':'blue',
    'height':'average',
    'profession':'nerd',
    'given_name':'ada'
}

for key in people:
    print(key, people[key]['profession'])

```