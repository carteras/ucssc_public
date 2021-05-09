from random import choice


test_string = 'the quick red fox jumped over the lazy hound'
upper_test_string = test_string.upper()
random_test_string = ''.join(choice((str.upper, str.lower))(c) for c in test_string)
options = ('--upper', '--lower', '--title', '--capitalize', '-u', '-l', '-t', '-c')

test_strings = [test_string, upper_test_string, random_test_string]

for test in test_strings:
    for option in options:
        print(f'python .\week13a_challenge1.py "{test}" {option}')