from hashlib import md5, sha256

def make_hash(file_name, algorithm='md5'):
    out = md5()
    if algorithm == 'sha256':
        out = sha256()
    with open(file_name, 'rb') as file_reader:
        while (byte := file_reader.read(1)):
            out.update(byte)
    return out.hexdigest()

hash_objects = {
    'plane': 'C:/Users/carte/Desktop/github/ucssc/2021/Digital Technologies - Digital Solutions/T2/hashing/plane.jpg',
    'ship' : 'C:/Users/carte/Desktop/github/ucssc/2021/Digital Technologies - Digital Solutions/T2/hashing/ship.jpg'
}

for key in hash_objects:
    print(f'{key}\t{make_hash(hash_objects[key])}')

