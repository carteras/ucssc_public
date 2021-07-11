words = ['bob', 'fred']

def is_isogram(word):
    # out = False
    set_of_word = set(word)
    for letter in set_of_word:
        if word.count(letter) > 1:
            return False
    return True

def is_palindrome(word):
    return word == word[::-1]
