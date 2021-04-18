def is_isogram(word):
    """A word in which no letter of the alphabet occurs more than once."""
    for letter in word:
        if word.count(letter) > 1:
            return False
    return True

def is_palindrome(word):
    """A word, sentence, or longer written work that reads the same backwards"""
    if word == word[::-1]:
        return True
    return False


words = ['dermatoglyphics', 'anna', 'adam']

for word in words:
    out = 'is neither a isogram or a palindrom'
    if is_isogram(word): 
        out = 'is an isogram'
    elif is_palindrome(word):
        out = 'is a palindrome' 
    print(f'Hey {word} {out}.')