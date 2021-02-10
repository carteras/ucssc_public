# F-Strings, Variables and Orders of Operations

## Goals


* Know what variables are and how to implement them for foundation cases
* * Understand basic orders of operations in relation to variables. 
* Changing variable types
* Know what f-strings are and how to use them
* How to accept user input. 


## Introduction

To get a better understanding of what is happening in python we will break up `hello_world`. 

```python
print("Hello, World!")
```

When you run this code you will see: 

```
> Hello, World!
```

As I mentioned before, `"Hello, World"` is a string, a blob of alpha-numeric or special characters. We can pull it out of the print statement and define it as it's own variable. 

```python
message = "Hello, World!"
print(message)
```

When you run this code you will see: 

```
> Hello, World!
````

### variables

What we've done is added a variable named message. All variables contain two things: 

* a name/label - how we, the programmer, asks python for some data
* a value - the data that python is storing for us. 

In this case, the name is called `message` and the value that it points to is a string that says `"Hello, World!"`

Let's play with this: 

**practice**

```python
name = 'Ada Lovelace'
age = "28"
fact = "Regarded as the first programmer."
print(name)
print(age)
print(fact)
```

You'll get the following output: 

```
> Ada Lovelace
> 28
> Regarded as the first programmer.
```

That's pretty cool, but can we add some more details to it? 

We could use that trick of using two strings
```python
name = 'Ada Lovelace'
age = "28"
fact = "Regarded as the first programmer."
print("Name: ", name)
print("Age: ",age)
print("Facts: ",fact)
```
```
> Name: Ada Lovelace
> Age: 28
> Facts: Regarded as the first programmer.
```

Neat trick! 

We can also join strings together and we can do so in two ways. 

```python
# note the space after the colon (:) and the + between strings
print("Name: " + name)
print("Age: " + age)
print("Facts: " + fact)
```

We can also join (concatenate) strings when we make variables

```python
name = 'Ada Lovelace'
age = "28"
fact = "Regarded as the first programmer."

name = "Name: " + name
age = "Age: " + age
fact = "Facts: " + fact

print(name)
print(age)
print(fact)
```

Wait, what wizardry did I just perform here? I added the data in the variable name to the end of a new string that says `"Name: "` and assigned that to the variable name. 

It's a bit like saying this 

```
x = 1
x = x + 1
print(x)
> 2
```

Variables can represent many different types of data. We've been introduced to string but there is more, a lot more. 

The first lot of variables we are going to use are:

* string: Text
* Numbers: integers (whole numbers) and float (numbers with decimal values)
* Boolean: True or False statements. 

### orders of operation

Let's talk maths.

Parentheses have the highest precedence and can be used to force an expression to evaluate in the order that you want. `2 * (3-1) == 4`

Exponentiation has the next highest precedence so `2**2+1 == 5` but `2**(2+1) == 8`

Multiplication and division operators have the same precedence, which is higher than addition and subtraction (which also have the same precedence with each other). Operators with the same precedence (except for `**`) are evaluated from left-to-right (left associative)

* `2 * 3 - 2 + 1 == 5`
* `(2*3) - 2 + 1 == 5`
* `6 - 2 + 1 == 5`
* `(6-2) + 1 == 5`
* `4 + 1 == 5`
* `5 == 5`

Let's talk python operators 

* `*` Multiplication - the repetition of addition (`2 * 4 = 2 + 2 + 2 + 2` )
* `/` Division  - the number of times you can separate some value into parts e.g., `8 / 2 == 4` because `2 + 2 + 2 + 2`
* `//` Floor division - Floor division is a normal division operation except that it returns the largest possible integer. This integer is either less than or equal to the normal division result. `7 // 3 == 2`
* `+` addition `1 + 1 == 2`
* `-` subtraction `2 - 1 == 1`
* `**` exponential `2**4 == 2 * 2 * 2 * 2 = 16`
* `%` modulus - In computing, the modulo operation returns the remainder or signed remainder of a division `7 % 3 = 7/3 = 2 remainder 1 = 1`
* = assigns a value `foo = 5` the variable, foo, is assigned the value of 5

Sometimes we want to reassign a variable. Let's say that we have a spaceship that is moving along the x axis. 

+= the logical equivalent to `foo = foo + 5` this is the same for other athematic values (`-=` `*=`, `/=`, etc)

```python 
x = 5
y = 5 

print(x, y)  # x -> 5, y -> 5

x = x + 1
print(x, y)  # x -> 6, y -> 5
```
 


**Practice**
```python
x = 15
y = 4

# Output: x + y = 19
print('x + y =',x+y)

# Output: x - y = 11
print('x - y =',x-y)

# Output: x * y = 60
print('x * y =',x*y)

# Output: x / y = 3.75
print('x / y =',x/y)

# Output: x // y = 3
print('x // y =',x//y)

# Output: x ** y = 50625
print('x ** y =',x**y)
```

### Changing variable types 

Often, you will want to use a variable's value within a message. For example, you might want to do something like this: 

```python
name = "ada lovelace"
age = 26
message = name.title() + " became the worlds first programmer at the age of " + age
print(message)
```

Wack that into code and run it.

You'll get the following error: 

```
Traceback (most recent call last):
  File "d:\github\ucssc\foo.py", line 3, in <module>
    message = name.title() + " became the worlds first programmer at the age of " + age
TypeError: can only concatenate str (not "int") to str
```

Type Errors mean that Python can't recognize the kind of information that you are using. In this example, you are using a number but Python isn't sure how to interpret it. 

We can tell python how to use this as a str by casting it with `str()`.

```python
name = "ada lovelace"
age = 26
message = name.title() + " became the worlds first programmer at the age of " + str(age)
print(message)
```
```
> Ada Lovelace became the worlds first programmer at the age of 26
```

You can also cast strings to numbers (you'll need this later!). Why is this important? Because you can sometimes get input in string format that you want to do maths stuff with. 


Let's look at this example. 
```python
x = "5"
print(x * 5)
```

You'd expect it to return 25 right? Here's what it returns: 

`> 55555`

Why is that? Remember that a String isn't a number. It might look like a number but Python uses it as a symbol that just happens to look like a number. So, how can we convert it into a number? In this case, we can use `int()` (because 5 is a whole number)
```python
x = "5"
print(int(x) * 5)
```
`> 25`

You could also reassign x: 

```python 
x = "5"
x = int(x)
print(x * 5)
```

### f-strings

One of the problems with string joining is that life can get very message. Let's rewrite our little set of facts about Ada Lovelace into a small story. 

```python
name = 'Ada Lovelace'
age = "28"
fact = "regarded as the first programmer"

story = "at the tender age of " + age + ", " + name + " started her work which would later see her " + fact + "."

print(story)
```

This is getting a bit chunky. Python 3.6 introduced a new way of handling  these kinds of outputs called f-strings. 

```python
name = 'Ada Lovelace'
age = 28
fact = "regarded as the first programmer"

story = f"At the tender age of {str(age)}, {name} started her work which would later see her {fact}."

print(story)
```

The advantage of f-strings is that by, effectively, injecting the variable directly into a string, it is a more elegant, and readable approach to joining strings. 

### User Input

In Python we can ask the user for input using the `input()` function. 

```python
message = input()
print(message)
```

## Challenges

### Challenge 1
 Using the following code as a base: 
 
 ```python
 name = input()
 name = name.strip()
 print(name)
 name = input()
 name = name.strip()
 print(name)
 name = input()
 name = name.strip()
 print(name)
 ```
 
 The output you must get is 
 
 `Hello, <name>, how are you?`
 
### Challenge 2

Using the following code: 

```python
name = input()
name = name.strip()
```

Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase,  titlecase, and capitalization. 

The input you will get is `ada lovelace`

### Challenge 3

Using the following code as a base: 

```python
name = input()
quote = input()
name = name.strip()
name = name.strip()
print(quote, name)
```

You are going to receive three famous quotes from 3 famous people. The format of your output must look like this: 

`<name> once said, "<quote>."`
All names must be in title case
all quotes must be capitalised 
e.g.: 
`Albert Einstein once said, “A person who never made a mistake never tried anything new.”`

The inputs you should are

albert einstein
I have no special talent. I am only passionately curious
BUDDHA
all that we are is the result of what we have thought
Steve jobs
STAY HUNGRY, STAY FOOLISH

### Challenge 4

Fix the following code: 

```python
# The programmer wants to create a simple calculating machine. 
# They want to add the first number to the second number. 
# It isn't working as intended. Please fix
first = input()
first = first.strip()
second = input()
second = second.strip()
print(first + second)
```

You will get two numbers and they must add up. i.e., `print(1 + 1)` must print `2`