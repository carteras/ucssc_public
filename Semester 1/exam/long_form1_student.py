def is_isogram(word):
    for letter in word:
        if word.count(letter) > 1:
            return False
    return True

def is_palindrome(word):
    if word == word[::-1]:
        return True
    return False

words = ['dermatoglyphics', 'anna', 'adam']
for word in words:
    out = ''
    if is_isogram(word):
        out = 'is an isogram'
    elif is_palindrome(word):
        out = 'is a palindrome'
    else:
        out = 'is neither an isogram or a palindrome'
    print(f'Hey, {word} {out}.')