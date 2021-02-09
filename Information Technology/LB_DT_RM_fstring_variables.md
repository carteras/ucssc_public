# F-Strings, Variables and Orders of Operations

## Goals


* Know what variables are and how to implement them for foundation cases
* Know what f-strings are and how to use them
* Understand basic orders of operations in relation to variables. 
* Changing variable types


## Introduction

To get a better understanding of what is happening in python we will break up `hello_world`. 

```python
print("Hello, World!")
```

When you run this code you will see: 

```
> Hello, World!
```

As we mentioned before, `"Hello, World"` is a string, a blob of alpha-numeric or special characters. We can pull it out of the print statement and define it as it's own variable. 

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

** TODO 
Python Assignment Operators
* =
* +=
* -=
* *=
* /=
* %=
* //=
* **=
* &=
* !=
* ^=


**Practice**



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
age = "28"
fact = "regarded as the first programmer"

story = f"At the tender age of {age}, {name} started her work which would later see her {fact}."

print(story)
```

The advantage of f-strings is that by, effectively, injecting the variable directly into a string, it is a more elegant, and readable approach to joining strings. 








### Changing variable types 


## Examples


## Practice

## Challenges