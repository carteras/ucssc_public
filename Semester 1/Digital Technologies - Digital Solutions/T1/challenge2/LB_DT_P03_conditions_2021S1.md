# Conditions 

## Introduction 
Python often involves examining a set of conditions and deciding which actions (if any) to take based on those conditions. 

## if

The simplest structure for a decision is the if statement. 

In an if statement, we can decide if something is true do one thing, otherwise do something else. 


```python
def test_equivalence(a, b):
    if a == b: 
        return f"{a} and {b} are equivalent"
    return f'{a} and {b} are not equivalent'

print(test_equivalence(5, 6))
print(test_equivalence(4, -4))
print(test_equivalence(1, 1))
print(test_equivalence(True, True))
print(test_equivalence(False, False))
```
```
5 and 6 are not equivalent
4 and -4 are not equivalent
1 and 1 are equivalent
True and True are equivalent
False and False are equivalent
```

We can also test if something is not equivalent. 
```python
def test_nonequivalence(a, b):
    if a != b: 
        return f"{a} and {b} not equivalent"
    return f'{a} and {b} are  equivalent'

print(test_nonequivalence(5, 6))
print(test_nonequivalence(4, -4))
print(test_nonequivalence(1, 1))
print(test_nonequivalence(True, True))
print(test_nonequivalence(False, False))
print(test_nonequivalence('Cats', 'Dogs'))
```
Less than and greater than operators, the same as maths, can be used to test if values are larger or smaller. 
```python 
def multiple_conditions(age_limit, name, your_age):
    if your_age < age_limit:
        return f"Sorry {name.title()}, you can't come in until you turn {age_limit}"

print(multiple_conditions(18, "ada", 17))
```



## multiple conditions 

Often, we encounter multiple variables must be tested. 
```python
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print(True or True)
print(True or False)
print(False or True)
print(False or False)
```

An example of an anded or ored statement might look like this: 

```python
pet_type = "cat"
pet_age = 7

if pet_type == cat and pet_age < 10:
    print("what a cute kitty")
else:
    print("what a nice old kitty")
```


## if else 

It is possible, and often desirable, to have two clearly branching steps. 

We can accomplish this with `if` and `else`
```python
def multiple_conditions(age_limit, name, your_age):
    if your_age < age_limit:
        return f"Sorry {name.title()}, you can't come in until you turn {age_limit}"
    else: 
        return f"Welcome {name.title()}, as you are {your_age - age_limit} years older than the limit, you may enter"
print(multiple_conditions(18, "ada", 21))
```

## if elif else 

What happens if we have multiple mutually exclusive statements? We can use `elif` (short for else if)

```python
def price_of_admission(age):
    price = 10.0
    if age < 4:
        return 0
    elif age < 18:
        return price/2
    else:
        return price

name = 'ada'
age = 16

print(f'{name} your price of admission is ${price_of_admission(age)}.')
```

## if elif elif 

This can be strung multiple times. 

```python
def price_of_admission(age):
    price = 10.0
    if age < 4:
        return 0
    elif age >= 4 and age <= 12:
        return price/4
    elif age < 18:
        return price/2
    else:
        return price

name = 'ada'
age = 16

print(f'{name} your price of admission is ${price_of_admission(age)}.')
```

## multiple conditions 

Something to be aware of is that sometimes you need to test multiple conditions that may not be mutually exclusive. This can lead to some oddities. 

```python
def foo(some_number):
    if some_number > 1:
        print(f'{some_number} is > 1')
    if some_number < 10:
        print(f'{some_number} is < 10')
    if some_number == 5: 
        print(f'{some_number} is == 5')

foo(5)
foo(4)
foo(6)
```