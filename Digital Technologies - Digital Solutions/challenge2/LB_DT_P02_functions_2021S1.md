# Functions

## Introduction 

Functions are named blocks of code that are designed for one specific job. Anytime you want to perform a particular task, you should define a function. To use that function we *call* that function responsible. 

Why use functions? The main reason is that if you need to perform a task multiple times, you don't need to code that task repeatedly. Instead, you can just call your function, and it does its magic. It's also a nifty way to break up more complicated problems. 

## Defining a function

Let's do a simple example of saying hi to a user: 

```Python
def print_hi():
    ''' Say hi to a user '''
    print("hello!")
```

This is the simplest structure of a function. 

`def` is a keyword that informs Python that you are defining a new function. It tells Python what kind of information the function needs to do its job. That's what the `()` is for if you have information for the function you put it in there. We've used that before with `print('hello, world!')`. This first line is called the function signature. 

After the function signature, we have the function body. The function body is where the heavy lifting is completed. The triple comment is called a docstring. We write that so we can generate documentation for our code. The line `print('hello!')` is the only line of meaningful code. 

To call this code all we need to do is call it. We've done this before with normal print statements so let's do this with print_hi: `print_hi()`


## Passing information to the function

Let's make a new print statement.  In this example, we want to have a customised greeting for new users to our system. By adding a username in the function definition, we can tell Python to accept a value of a username and then do something with it. In this case, we will print it to standard output. 

```python
def hello_user(username):
     '''displays a simple greeting to a user'''
    print(f"Hello, {username.title()}! How are you?")

hello_user("ada lovelace")
hello_user("bob bobbington")
hello_user("charles babbage")
```

## passing arguments

When you call a function, Python must match each argument in the function call with a function definition parameter. The simplest way to do this is based on the order of the arguments provided. Values matched up this way are called positional arguments. To see how this works, consider a function that displays information about DnD characters. The function tells us what role each character is and what their name is. 

```python
def describe_character(character_name, character_role):
    '''display information about a character '''
    print(f'My name is {character_name.title()}.')
    print(f"My role is {character_role} and I am awesome!")

describe_character("Bob", "Fighter")
describe_character("Alice", "Rogue")
describe_character("Morgan", "Magic User")
describe_character("Justice", "Lord high poobar of the third realm")
```
## keyword order and default values
You can get unexpected results if you mix up the order of the arguments in a function call when using positional arguments. Try the following:
`describe_character("Rogue", 'Alice')`

My friend Alice would probably find that pretty funny. 

But the question that comes to mind is: How do we handle putting content in backwards? Can we even handle content going in backwards? 

Yes: 

```python
def describe_character(character_name, character_role):
    '''display information about a character '''
    print(f'My name is {character_name.title()}.')
    print(f"My role is {character_role} and I am awesome!")
    print("-"*80)

describe_character(character_role="Rogue", character_name='Alice')
```
We can use the arguments as keyword arguments. You directly associate the name and the value with the argument. So, when you pass the argument to the function, there is no confusion (You won't end up with an Alice called Rogue. 

# Default values

Sometimes we need to declare two (or more) variables in the function definition but one (or more) might generally be something. Like, maybe 90% of characters are actually fighters. How do we handle this so we can type less but still handle edge cases? We can simply give the variable a default value. 

```python
def describe_character(character_name, character_role = "fighter"):
    '''display information about a character '''
    print(f'My name is {character_name.title()}.')
    print(f"My role is {character_role} and I am awesome!")
    print("-"*80)

describe_character("Bob")
describe_character("Morgan", "Magic User")
describe_character("Justice")
describe_character(character_role="Rogue", character_name='Alice')
```
## Return values 

Generally speaking, we won't want to just print things to standout output. It's commonly seen as a poor form outside of logging errors. 

So, how can we handle it? Well, we return the details from the function. 

```python
def describe_character(character_name, character_role = "fighter"):
    '''display information about a character '''
    out = f'My name is {character_name.title()}.\n'
    out +=f"My role is {character_role} and I am awesome!\n"
    out += "-"*80
    return out

my_char = describe_character("Bob")
print(my_char)
```

Actually, using that as an example probably isn't the best solution. Let's do some maths: 

```python
def area_rectangle(width, length):
    '''get the area of a rectangle'''
    return width * length

print(area_rectangle(5, 5))
```

