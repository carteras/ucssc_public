from pathlib import Path
from hashlib import md5, sha256

def make_hash(file_name, algorithm='md5'):
    out = md5()
    if algorithm == 'sha256':
        out = sha256()
    with open(file_name, 'rb') as file_reader:
        while (byte := file_reader.read(1)):
            out.update(byte)
    return out.hexdigest()

my_file_directory = Path().cwd() / "2021/Digital Technologies - Digital Solutions/T2/hashing"

hash_objects = {
   
    'plane': my_file_directory / 'plane.jpg',
    'ship' : my_file_directory / 'ship.jpg'
}


for key in hash_objects:
    ho = hash_objects[key]
    print(f'Directory: {ho.parent}')
    print(f'File name: {hash_objects[key].name}') 
    print(f'hash: {make_hash(hash_objects[key])}')
    

