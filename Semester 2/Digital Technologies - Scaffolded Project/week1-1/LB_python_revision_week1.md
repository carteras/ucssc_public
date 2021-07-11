# Title

## You will learn

## The Zen of Python

![](2021-07-11-15-18-19.png)

### Math Operators

|Operator|Operation|Example|
|:--|:--|:--|
|**	|Exponent	|2 ** 3 = 8|
|%	|Modulus/Remainder	|22 % 8 = 6|
|//	|Integer division	|22 // 8 = 2|
|/	|Division	|22 / 8 = 2.75|
|*	|Multiplication	|3 * 3 = 9|
|-	|Subtraction	|5 - 2 = 3|
|+	|Addition	|2 + 2 = 4 |


### Data Types

|Data Type | Example| 
|:--|:--|
|Integer|-2, -1, 0, 1, 2, 3|
|Floating point number|-1.25, -1.0, --0.5, 0.0, 0.5, 1.0, 1.25|
|Strings|'a', 'aa', 'aaa', 'Hello!', '11 cats'|

### String Concatenation and Replication

Concatenation
```python
a = 'foo'
b = 'bar'
print(a+b)
```
Stay away from `+`. Please prefer string formatting (`f-string`)

Replication
```python
name = 'Ada'
print(name*5)
```

### Variables
You can name a variable anything as long as it obeys the following rules:

* It can be only one word.
* It can use only letters, numbers, and the underscore (_) character.
* It can’t begin with a number.
* Variable name starting with an underscore (_) are considered as "unuseful`.

Example: 
```python
name = 'Ada'
print(name)
```
### Commenting
in line comment: 
```python
# This is a comment
```

Multiline comment: 

```python
# haha tricked you
# We just comment each line
```

Code with a comment in line: 

```python
a = 1               # initializing 1
```

Function document string: 
```python
def foo():
    """
    This is a function docstring
    You can also use:
    ''' Function Docstring '''
    """
```
### Printing stuff
```python
print('Hello world!')
```

```python
name = 'ada'
print('Hello world!', ada)
```
### Accepting input
```python
print("What is your name?")
name = input()
print(f"it is good to meet you, {name}")
```
### Getting the length of something 
Counting the number of letters in strings or things in a list
```python
print(len('hello'))
```
Testing the emptiness of a list
```python
foo = [1, 2, 3]
if foo:
    print("This list is not empty")
else:
    print("This list is empty")
```
### The str(), int(), and float() Functions
```python
# Change a number to a string
print(str(29))
```
```python
age = 9001
print(f'I am {str(age)} years old.')
```
```python
print(str(-3.14))
```
Change Floats to Integer

```python
print(int(5.6))
```
```python
print(int(5.6)+1)
```
Strings to numbers
```python
print(int("1")+1)
```
```python
print(float("1")+1)
```
### Flow Control
Comparison operators
|Operator| meaning|
|:--|:--|
|==	|Equal to|
|!=	|Not equal to|
|<	|Less than|
|>	|Greater Than|
|<=	|Less than or Equal to|
|>=	|Greater than or Equal to|

These operators evaluate to True or False depending on the values you give them.


```python
print(42 == 42)
```
```python
print(42 == 41)
```
```python
print('hello' == 'hello')
```
```python
print('hello' == 'Hello')
```
```python
print('dog' != 'cat')
```
```python
print(42 == 42.0)
```
```python
print(42 == '42')
```
### Boolean evaluation 
Never use == or != operator to evaluate boolean operation. Use the is or is not operators, or use implicit boolean evaluation.

NO (even if they are valid Python):

```python
print(True == True)
print(True != False)
```
YES (even if they are valid Python):
```python
print(True is True)
print(True is not False)
```
These statements are equivalent:
```python
a = True

if a is True:
    pass
if a is not False: 
    pass
if a:
    pass
```

### Boolean operators
There are three Boolean operators: and, or, and not.

The and Operator’s Truth Table:

|Expression| Evaluates to|
|:--|:--|
|True and True	|True
|True and False	|False
|False and True	|False
|False and False	|False

The or Operator’s Truth Table:
|Expression| Evaluates to|
|:--|:--|
|True or True	|True
|True or False	|True
|False or True	|True
|False or False	|False

The not Operator’s Truth Table:
|Expression| Evaluates to|
|:--|:--|
|not True	|False
|not False	|True

### Mixing Boolean and Comparison Operators
```python
print((4 < 5) and (5 < 6))
```
```python
print((4 < 5) and (9 < 6))
```
You can also use multiple Boolean operators in an expression, along with the comparison operators:

```python
print(2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2)
```

### Logical Flow
if statements
```python
if name == 'Alice':
    print('Hi, Alice.')
```
else statements
```python
name = 'Bob'
if name == 'Alice':
    print('Hi, Alice.')
else:
    print('Hello, stranger.')
```
elif
```python
name = 'Bob'
age = 5
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
```
```python
name = 'Bob'
age = 30
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice nor a little kid.')
```
### While loop statements
```python
spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1
```
### Break statement
```python
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')
```
### Continue statements
```python
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
```
### for Loops and the range() Function
```python
print('My name is')
for i in range(5):
    print(f'Jimmy Five Times ({str(i)})')
```
The range() function can also be called with three arguments. The first two arguments will be the start and stop values, and the third will be the step argument. The step is the amount that the variable is increased by after each iteration.

```python
for i in range(0, 10, 2):
    print(i)
```
```
0
2
4
6
8
```
You can even use a negative number for the step argument to make the for loop count down instead of up.


```python
for i in range(10, 0, -2):
    print(i)
```
```
10
8
6
4
2
```
### For else statment
This allows to specify a statement to execute in case of the full loop has been executed. Often only useful when a break condition can occur in the loop:

```python
for i in [1, 2, 3, 4, 5]:
    if i == 3:
        break
else:
    print("executes when no item of the list equals to 3")
```
### Importing modules
```python
import random
for i in range(5):
    print(random.randint(1, 10))
```
```python
import random, sys, os, math, pathlib, argparse
```
```python
from random import *

```
```python
from random import randint
```
```python
from random import randint as ri
print(ri(1, 100))
```
### Killing programs early
```python
import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print(f'You typed {response}.')
```
### Functions
```python
def hello(name):
    print(f"Hello {name}!")

hello("Alice")
hello("Bob")
hello("Charlie")
```
### Return Values and return Statements
When creating a function using the def statement, you can specify what the return value should be with a return statement. A return statement consists of the following:

The return keyword.

The value or expression that the function should return.
```python
import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
```
### Keyword Arguments and print()

```python
print('Hello', end='')
print('World')
```
```python
print('cats', 'dogs', 'mice')
```
```python
print('cats', 'dogs', 'mice', sep=',')
```
### Local and Global scope
Code in the global scope cannot use any local variables.

However, a local scope can access global variables.

Code in a function’s local scope cannot use variables in any other local scope.

You can use the same name for different variables if they are in different scopes. That is, there can be a local variable named spam and a global variable also named spam.
### The global Statement
If you need to modify a global variable from within a function, use the global statement:


```python
def spam():
    global eggs
    eggs = 'spam'

eggs = 'green eggs'
spam()
print(eggs)
```
There are four rules to tell whether a variable is in a local scope or global scope:

If a variable is being used in the global scope (that is, outside of all functions), then it is always a global variable.

If there is a global statement for that variable in a function, it is a global variable.

Otherwise, if the variable is used in an assignment statement in the function, it is a local variable.

But if the variable is not used in an assignment statement, it is a global variable.
### Lists
```python

```
### Detail
```python
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam)
```
### Getting Individual Values in a List with Indexes

```python
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[0])
print(spam[1])
```
### Negative Indexes

```python
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[-1])
```
### Getting Sublists with Slices

```python
spam = ['cat', 'bat', 'rat', 'elephant']
spam[0:4]
spam[1:3]
spam[0:-1]
spam[:2]
spam[1:]
```
Slicing the complete list will perform a copy:
```python

```

### Detail
```python
spam2 = spam[:]
spam.append('dog')
print(spam)
print(spam2)
```
### Length of a list
```python
spam = ['cat', 'dog', 'moose']
len(spam)
```
### Changing Values in a List with Indexes

```python
spam = ['cat', 'bat', 'rat', 'elephant']
spam[1] = 'aardvark'
```
### List Concatenation and List Replication
```python
spam = [1, 2, 3] + ['A', 'B', 'C']
print(spam)
spam = [1, 2, 3]*3
print(spam)

```
### Removing Values from Lists with del Statements

```python
spam = [1, 2, 3]
del spam[1]
print(spam)
```
### Using for Loops with Lists

```python
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']

for supply in supplies:
    print(f"The item is {supply}")

for i, supply in enumerate(supplies):
    print(f"The {i} in the list is a {supply}")
```
### Looping Through Multiple Lists with zip()

```python
names = ['Pete', 'John', 'Elizabeth']
ages = [6, 23, 44]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```
### The in and not in Operators

```python
'howdy' in ['hello', 'hi', 'howdy', 'heyas']
```
```python
spam = ['hello', 'hi', 'howdy', 'heyas']
print('cat' in spam)
```
```python
spam = ['hello', 'hi', 'howdy', 'heyas']
print('howdy' not in spam)
```
```python
spam = ['hello', 'hi', 'howdy', 'heyas']
print('cat' not in spam)
```
### Augmented Assignment Operators
|Operator|Equivalent|
|:--|:--|
|spam += 1	|spam = spam + 1
|spam -= 1	|spam = spam - 1
|spam *= 1	|spam = spam * 1
|spam /= 1	|spam = spam / 1
|spam %= 1	|spam = spam % 1
```python
spam = 'Hello'
spam += ' world!'
print(spam)
```
### Finding a Value in a List with the index() Method

```python
spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
print(spam.index('Pooka))
```
### Adding Values to Lists with the append() and insert() Methods

```python
spam = ['cat', 'dog', 'bat']
spam.append('moose')
print(spam)
spam.insert(1, 'chicken)
print(spam)
```
### Removing Values from Lists with remove()

```python
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
print(spam)
```
### Dictionaries and Structuring Data

```python
myCat = {'size': 'fat', 'color': 'black and white', 'disposition': 'loud'}
```
### The keys(), values(), and items() Methods
values():

```python
spam = {'colour': 'red', 'age': 42}
for v in spam.values():
    print(v)
```
keys():
```python
spam = {'colour': 'red', 'age': 42}
for k in spam.keys():
    print(k)
```
items():
```python
spam = {'colour': 'red', 'age': 42}
for i in spam.items():
    print(i)
```

iterating
```python
spam = {'color': 'red', 'age': 42}
for k in spam:
    print(k)
```
Using the keys(), values(), and items() methods, a for loop can iterate over the keys, values, or key-value pairs in a dictionary, respectively.

```python
spam = {'color': 'red', 'age': 42}
for k, v in spam.items():
    print(f'Key: {k} Value: {str(v)}')
```
### Checking Whether a Key or Value Exists in a Dictionary

```python
spam = {'name': 'Zophie', 'age': 7}
print('name' in spam.keys())

print('Zophie' in spam.keys())
```
## Dictionary and Knowledge Corner 
* When was Python released? 
* What was the name of the person who wrote it? 
* Why do you think whitespace is so important in python?
* Why might readability be so important in Python? 
* Describe some of the rules of naming variables

## Challenges

#### Create a program that can  print out the following text: 
“Hello world”
“Hello again”
“Printing is fun!”
“Yay! Printing”

#### Create a program that given the following variables
```python
hens = 25 + 30 / 6
roosters = 100 - 25 * 3
```
Prints the following
> “I will now count my chickens”
> “Hens 30”
> “Roosters 25.0”

#### Complete the following program
Using the following code: 
```python
cars = 100
space_in_cars = 4
drivers = 30
passengers = 90
```
* How many cars can be driven? 
* Are there enough cars to drive everybody? 
* What is the fewest number of cars that can be driven to transport everybody
* How many cars are either left over or needed to complete the transfer in one trip?

### Intermediate Challenges
* Create a program that can accept user input. 
* The input you are after is given_name, family_name, and age
* Input looks like this: "Adam carter 9001"
* The program is not restricted by the number of inputs
* The end of inputs is defined by the command end_list
* When your program has received the end of the lists, it then prints all of the names
* Each line must be printed with appropriate titles. 

### Advanced Challenges

You’ve been hired to write some simple software for your teacher. You need to create a program processes a list of student from a file. This file consists of the students name and scores. Your program will also use functions to find the following: 

* The min, max, mean, median, and mode, scores of the class. 
* Which students got the min, max, mean, median, and mode, scores of the class (or closest you can)

Also, your teacher is kind of weird. They also want to know the following: 
* Which students have the longest names, given names, family names, and both names. 
* Which students have the shortest names, given, family, and both. 
* They also love the letter A. They want to know which student has the most As in both names. 


