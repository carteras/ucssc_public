from hashlib import md5

def hash_text(string_in):
    msg = md5()
    msg.update(string_in.encode('utf-8'))
    return msg.hexdigest()

print(hash_text("hello world"))


