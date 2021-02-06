# Variables

```python
message = "Hello world!"
print(message)
```

Naming and Using Variables
When you’re using variables in Python, you need to adhere to a few rules

and guidelines. Breaking some of these rules will cause errors; other guide-
lines just help you write code that’s easier to read and understand. Be sure to keep the following variable rules in mind:

• Variable names can contain only letters, numbers, and underscores.
They can start with a letter or an underscore, but not with a number.
For instance, you can call a variable message_1 but not 1_message.
• Spaces are not allowed in variable names, but underscores can be used
to separate words in variable names. For example, greeting_message works,
but greeting message will cause errors.
• Avoid using Python keywords and function names as variable names; that is, do not use words that Python has reserved for a particular pro-
grammatic purpose, such as the word print. 
• Variable names should be short but descriptive. For example, name is
better than n, student_name is better than s_n, and name_length is better
than length_of_persons_name.
• Be careful when using the lowercase letter l and the uppercase letter O
because they could be confused with the numbers 1 and 0.

It can take some practice to learn how to create good variable names,
especially as your programs become more interesting and complicated. As
you write more programs and start to read through other people’s code,
you’ll get better at coming up with meaningful names.



Let's do some maths: 
```python
print(3+2) # 3 + 2 = 5
print(3-2) # 3 - 2 = 1
print(3*2) # 3 * 2 = 6
print(3/2) # 3 / 2 = 1.5 (be careful of old versions)
print(3**2)# 3^2 = 3*3 = 9
print(3%2) # 3%2 = 1 (3/2 = 1 with 1 remaining
```

### Printing a variable:   
```python
foo = "output"
print(foo)
```


Getting user input: 
```python
name = input('Hey, what is your name?")
print(name)
```

Converting between types: 
You can convert between data types using a technique called "casting". 

for example:
`foo = int("5")`
```python
foo = input("How many days are in the week? ")
foo = int(foo)
print(foo*3)
```

### Using f-strings
```python
given_name = 'Ada'
family_name = 'Lovelace
print(f"The first programmer's name was {given_name} {family_name}")
```