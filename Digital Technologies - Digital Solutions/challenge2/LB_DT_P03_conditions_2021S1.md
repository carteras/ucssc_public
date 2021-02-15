# Conditions 

## Introduction 
Python often involves examining a set of conditions and deciding which actions (if any) to take based on those conditions. 

## if
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

## multiple conditions 

```python 
def multiple_conditions(age_limit, name, your_age):
    if your_age < age_limit:
        return f"Sorry {name.title()}, you can't come in until you turn {age_limit}"

print(multiple_conditions(18, "ada", 17))
```

## AND and OR statements. 

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

## if else 
```python
def multiple_conditions(age_limit, name, your_age):
    if your_age < age_limit:
        return f"Sorry {name.title()}, you can't come in until you turn {age_limit}"
    else: 
        return f"Welcome {name.title()}, as you are {your_age - age_limit} years older than the limit, you may enter"
print(multiple_conditions(18, "ada", 21))
```

## if elif else 

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