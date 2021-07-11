



def terrible_hash(string_in):
    return hex(ord(string_in[0]))

def bad_hash(string_in):
    hash = 5381
    out = ''
    for letter in string_in:
        hash += ord(letter)
    return hex(hash & 0xFFFFFFFF)

def hash_djb2(s):
    hash = 5381
    for letter in s:
        hash = (( hash << 5) + hash ) + ord(letter)
    return hex(hash & 0xFFFFFFFF)

clear_text = 'the quick brown fox jumped over the lazy hound'
print(hash_djb2(clear_text))

# print(bad_hash(clear_text))

# print(terrible_hash(clear_text))





