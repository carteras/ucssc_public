# Lists and Working with lists

## Goals

### Lists

* What are lists?
* Why do we use lists?
* How can we create a list with stuff that we know?
* How can we access specific elements in a list?

### Working with lists

* What is iteration?
* How do we normally iterate in python? (for)
* How else can we iterate in python (while)

### Other stuff related to lists

* How can we get a sub-section of elements in a list? 
* What's this list thing with `()` brackets instead of `[]` brackets? 


## Lists
### Introduction
A list is a data-structure, or collection, of items in a particular order. Lists can contain the letters of the alphabet, numerical characters from 0-100, the names of people, or anything else you can put into python. It is even possible to add things to a list that aren't related (but I wouldn't recommend that)

Lists are defined as sitting between two square brackets `[]`. Here's an example: 

```python
weapons = ['dagger', 'sword', 'mace', 'axe']
print(weapons)
```
```
> ['dagger', 'sword', 'mace', 'axe']
```

### Making a list from a string

The easiest way for CTFd to generate a list is to split a string on some value. Here, I'll show you. In this example, we will split a string on the `,` character: 

```python
weapons = "dagger,sword,mace,axe"
print(weapons)
weapons = weapons.split(',')
print(weapons)
```
```
dagger,sword,mace,axe
['dagger', 'sword', 'mace', 'axe']
```

We could also split on other characters

```python
weapons = "dagger sword mace axe"
print(weapons)
weapons = weapons.split(' ')
print(weapons)
```
```
dagger,sword,mace,axe
['dagger', 'sword', 'mace', 'axe']
```

### Getting elements inside a list. 

Lists are ordered collections. This means that `'dagger'` will always be the first in the list. We can access that element by calling it's index (position) in the list. In this case, the first item in a number line is `0`. We call it using the square `[]` brackets. 

```python
weapons = ['dagger', 'sword', 'mace', 'axe']
print(weapons[0])
```
```
> dagger
```

For all intents and purposes this is the same as accessing a variable, so we can use functions attached to it. In this case, we are using strings, so we could use string functions. 

```python
weapons = ['dagger', 'sword', 'mace', 'axe']
print(weapons[0].title())
```
```
> Dagger
```

Likewise, that means we can use and abuse it: 

```python
weapons = ['dagger', 'sword', 'mace', 'axe']
message = f'I think my {weapons[3].title()} is the best!'
print(message)
```

Although, once you've created the variable it has been set in stone. So, even if the list changes, your message won't be interrupted.

```python
weapons = ['dagger', 'sword', 'mace', 'axe']
message = f'I think my {weapons[3].title()} is the best!'
weapons[3] = "spear"
print(message)
```

### Number lines start at 0

You might be wondering, why are we using 0 and not 1? We'll that's because number lines start at 0. 

```python
weapons = ['dagger', 'sword', 'mace', 'axe']
print(weapons[0].title())
print(weapons[1].title())
print(weapons[2].title())
print(weapons[3].title())
```

### Changing an element in a list

As mentioned above, you can modify an element in a list as you would a variable

```python
weapons = ['dagger', 'sword', 'mace', 'axe']
print(f'I think my {weapons[3].title()} is the best!')
weapons[3] = "spear"
print(f'I think my {weapons[3].title()} is the best!')
```

### Adding to a list

The simplest way to add to a list is to `append()` an item to the end. 

```python
weapons = ['dagger', 'sword', 'mace', 'axe']
print(weapons)
weapons.append("spear")
print(weapons)
```
```
['dagger', 'sword', 'mace', 'axe']
['dagger', 'sword', 'mace', 'axe', 'spear']
```

### Removing items from a list: 


Sometimes you will need to remove an item from a list. Maybe you have a list of potential password that you are using to brute force into a computer. Every time you fail to get entry you can remove the password so you don't waste your time in the future. 

To do this we use the `del` command: 

```python
weapons = ['dagger', 'sword', 'mace', 'axe']
print(weapons)
weapons.append("spear")
print(weapons)
del weapons[0]
print(weapons)
```
```
['dagger', 'sword', 'mace', 'axe']
['dagger', 'sword', 'mace', 'axe', 'spear']
['sword', 'mace', 'axe', 'spear']
```

You can also use the remove function. 

```python
weapons = ['dagger', 'sword', 'mace', 'axe']
print(weapons)
weapons.append("spear")
print(weapons)
del weapons[0]
print(weapons)
weapons.remove('axe')
print(weapons)
```

### Sorting lists

Sometimes you need to sort lists. Python comes with a sort tool `sort([list])`.

```python
weapons = ['dagger', 'sword', 'mace', 'axe']
print(weapons)
weapons.sort()
print(weapons)
```
```
['dagger', 'sword', 'mace', 'axe']
['axe', 'dagger', 'mace', 'sword']
```

We can use the same tool with an argument to reverse it: 

```python
weapons = ['dagger', 'sword', 'mace', 'axe']
print(weapons)
weapons.sort(reverse=True)
print(weapons)
```
```
['dagger', 'sword', 'mace', 'axe']
['sword', 'mace', 'dagger', 'axe']
```

Sometimes however, we don't want to permanently sort our list. We can use the `sorted([list])` function to handle that for us. 

```python
weapons = ['dagger', 'sword', 'mace', 'axe']
print(sorted(weapons), weapons)
```
```['axe', 'dagger', 'mace', 'sword'] ['dagger', 'sword', 'mace', 'axe']
```

Lastly, what happens if we just want to reverse the list and not sort it? 

```python
weapons = ['dagger', 'sword', 'mace', 'axe']
weapons.reverse()
print(weapons)
```


### Finding the length of a list? 

You will need to find the lengths of list a lot. Like a crazy number of times. In python it's pretty easy. We find the `len([list])`

```python
weapons = ['dagger', 'sword', 'mace', 'axe']
print(len(weapons))
```
```
4
```

## Working with lists

Right, you might be thinking to yourself, aren't programmers supposed to be lazy? Yes! Yes we are. How is storing things in a list supposed to be easy?

Well, we can get python to do much of the heavy lifting for us with a fancy tool called iteration. 

### Looping through an entire list

How do we loop through an entire list? Easy, python has a `for-each` command called `for`. 

```python
weapons = ['dagger', 'sword', 'mace', 'axe']
for weapon in weapons:
    print(weapon)
```

### Doing some heavy lifting in a loop

```python
weapons = ['dagger', 'sword', 'mace', 'axe']
for weapon in weapons:
    print(f"{weapon.title()}s look great!")
```
```
Daggers look great!
Swords look great!
Maces look great!
Axes look great!
```

### Making numerical lists

Python allows us to make a range of numbers using the `range()` function. 

By default, all it needs is the size it stops at (be warned, it stops before printing):
```python
for value in range(10):
    print(value)
```
```
0
1
2
3
4
5
6
7
8
9
```

You can define the starting position

```python
for value in range(5, 10):
    print(value)
```
```
5
6
7
8
9
```

And you can control how many steps you iterate by: 
```python
for value in range(5, 10, 2):
    print(value)
```
```
5
7
9
```

We can also make a list of numbers by casting the outcome of range to a list: 

```python
numbers =list(range(5, 10, 2))
print(numbers)
```

### While loops

For-each and even for loops are fairly new constructs. They are an abstraction of the following type of loop. 

```python
foo = list(range(0, 10))
i = 0
max_num = len(foo)
while i < max_num:
    print(i)
    i = i+1
```


## Other list stuff

### Min, Max, Sum, mean

Python has some functions to help us find some simple stats stuff

```python
foo = list(range(0, 100))
print(min(foo))
print(max(foo))
print(sum(foo))
print(sum(foo)/len(foo))
```

### Working with parts of a list

We've learnt elsewhere how to access a single element of a list and we've also worked with looking through all of the elements in a list. In python we can also work with sub-lists. We create sub-lists which python calls a slice. 

#### Slicing a list 

To specify a slice you need to identify the first and last elements of the sub-list. 

Let's say that only want the first two items in a list. 

```python
weapons = ['dagger', 'sword', 'mace', 'axe']
print(weapons[0:2])
```
```
['dagger', 'sword']
```

It's possible to play with any combination of a list. You could get the middle: 

```python
weapons = ['dagger', 'sword', 'mace', 'axe']
print(weapons[1:3])
```
The end of a list

```python
weapons = ['dagger', 'sword', 'mace', 'axe']
print(weapons[2:4])
```
### Looping through a slice

Once we've defined a slice we can slice through as if it is a normal list. 

```python
weapons = ['dagger', 'sword', 'mace', 'axe']

for weapon in weapons[2:4]:
    print(weapon)
```