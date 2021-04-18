def hello_user(username):
    '''displays a simple greeting to a user
    >>> hello_user("ada lovelace")
    Hello, Ada Lovelace! How are you?
    >>> hello_user("bob bobbington")
    Hello, Bob Bobbington! How are you?
    >>> hello_user("charles babbage")
    Hello, Charles Babbage! How are you?
    '''
    #pass      You need to make sure you remove pass. Pass returns None type
    username = username.strip()
    print(f"Hello, {username.title()}! How are you?")

hello_user(input())     #we need to make CTFd run the same test that the doctest used
hello_user(input())     #there were 3 tests so we need to run hello_user(input()) 3 times
hello_user(input())     #the input() is the data coming from CTFd