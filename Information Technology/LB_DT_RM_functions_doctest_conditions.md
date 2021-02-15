

## Challenges

### Are the Numbers Equal?
Create a function that returns True when num1 is equal to num2; otherwise return False.
```python
is_same_num(4, 8) ➞ False

is_same_num(2, 2) ➞  True

is_same_num(2, "2") ➞ False
```

Don't forget to `return` the result.

### Is the Number Less than or Equal to Zero?

Create a function that takes a number as its only argument and returns True if it's less than or equal to zero, otherwise return False.

Examples
```python
less_than_or_equal_to_zero(5) ➞ False

less_than_or_equal_to_zero(0) ➞ True

less_than_or_equal_to_zero(-2) ➞ True
```

## Profitable Gamble
Create a function that takes three arguments prob, prize, pay and returns True if prob * prize > pay; otherwise return False.

To illustrate:

`profitable_gamble(0.2, 50, 9)`
... should yield True, since the net profit is 1 (0.2 * 50 - 9), and 1 > 0.
```python
profitable_gamble(0.2, 50, 9) ➞ True

profitable_gamble(0.9, 1, 2) ➞ False

profitable_gamble(0.9, 3, 2) ➞ True
```

### THREE!!!!

Create a function that takes two arguments. Both arguments are integers, a and b. Return True if one of them is 3 or if their sum is 3.

```python
makes10(3, 6) ➞ True

makes10(1, 4) ➞ False

makes10(1, 2) ➞ True
```
## Multiple of 100
Create a function that takes an integer and return True if it's divisible by 100, otherwise return False.

```python
divisible(1) ➞ False

divisible(1000) ➞ True

divisible(100) ➞ True
```

## Compare Strings by Count of Characters
Create a function that takes two strings as arguments and return either True or False depending on whether the total number of characters in the first string is equal to the total number of characters in the second string.

NOTE: `len("adam") ➞ 4`

```python
comp("AB", "CD") ➞ True

comp("ABC", "DE") ➞ False

comp("hello", "edabit") ➞ False
```

## Is the Number Even or Odd?

Create a function that takes a number as an argument and returns "even" for even numbers and "odd" for odd numbers.

```python
isEvenOrOdd(3) ➞ "odd"
isEvenOrOdd(146) ➞ "even"
isEvenOrOdd(19) ➞ "odd"
```
## Area Finder
Write a function that accepts base (decimal), height (decimal) and shape ("triangle", "parallelogram") as input and calculates the area of that shape.

```python
area_shape(2, 3, "triangle") ➞ 3
area_shape(8, 6, "parallelogram") ➞ 48
area_shape(2.9, 1.3, "parallelogram") ➞ 3.77
```

## AND, OR and NOT
You will need to write three unfinished logic gates. Continue to write the three logic gates: AND, OR, and NOT.
```python
AND(1, 1) ➞ 1
AND(0, 0) ➞ 0

OR(1, 0) ➞ 1
OR(1, 1) ➞ 1

NOT(0) ➞ 1
NOT(1) ➞ 0
```

## Repeat String

Create a function that takes a string txt and a number n and returns the repeated string n number of times.

If given argument txt is not a string, return Not A String !!

```python
repeat_string("Mubashir", 2) ➞ "MubashirMubashir"

repeat_string("Matt", 3) ➞ "MattMattMatt"

repeat_string(1990, 7) ➞ "Not A String !!"
```

## Design a challenge (or more)

Using the content we have already been taught, create your own challenge. 

You can use input from the system 

And test the output from the system