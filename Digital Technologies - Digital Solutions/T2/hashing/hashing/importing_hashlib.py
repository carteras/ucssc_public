from hashlib import md5, sha1

passwords = [
    'password',
    'password!',
    'passw0rd'
]

def make_hash(pass_phrase, algorithm='md5'):
    m = None
    if algorithm == 'md5':
        m = md5()
    elif algorithm == 'sha1':
        m = sha1()
    else:
        return -1
    pass_phrase = pass_phrase.encode('utf-8')
    m.update(pass_phrase)
    return m.hexdigest()

password_hashes = {}

for password in passwords:
    password_hashes[password] = make_hash(password)

reverse_password_hashes = {}

for password, hashed_password in password_hashes.items():
    reverse_password_hashes[hashed_password] = password

password_table = ['fd820a2b4461bddd116c1518bc4b0f77', 'faf2ca38c02c5f2ba1c49d200a03f9fb', '823fec7a2632ea7b498c1d0d11c11377', '4badaee57fed5610012a296273158f5f', 'dc599a9972fde3045dab59dbd1ae170b', '5f0cbc3f99acb914d429cfdf23dd75e3', '63188b0436e754a4d9a1d89dfc978209', '5583413443164b56500def9a533c7c70', 'bed128365216c019988915ed3add75fb', 'fe01d67a002dfa0f3ac084298142eccd', 'b1f4f9a523e36fd969f4573e25af4540']

for pass_hash in password_table:
    if pass_hash in reverse_password_hashes:
        print(pass_hash, reverse_password_hashes[pass_hash])

