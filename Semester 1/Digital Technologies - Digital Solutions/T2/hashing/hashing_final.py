from pathlib import Path
from hashlib import md5, sha256

def make_hash(file_path, algorithm='md5'):
    """ creates either MD5 or SHA256 hashes from files
    
    This function takes the file_path of a file and creates a hash. The hash is selected as md5 as default but can be switched to SHA256 by using the algorithm keyword argument. 

    Parameters:
    file_path: a pathlib path of the file to be hashed
    algorithm: the type of algorithm to use for hashing. 

    Returns:
    Either an MD5 hash or a SHA256 hash of the given file.     
    """

    # selects MD5 by default. (is this optimum?)
    out = md5() 

    # if algorithm was sha256, switch to that. 
    if algorithm == 'sha256':
        out = sha256()

    # opens a file in read binary mode as file_reader
    with open(file_path, 'rb') as file_reader:
        # read a chunk of data from the file and assign it to byte
        while (byte := file_reader.read(out.block_size)):
            # update out with the chunk of data. 
            out.update(byte) 

    # return the hash as a hexdigest. 
    return out.hexdigest()

# Setting the directory to where hash objects are. 
my_file_directory = Path().cwd() / "2021/Digital Technologies - Digital Solutions/T2/hashing"

# hand crafting my dictionary. 
hash_objects = {
    'plane': my_file_directory / 'plane.jpg',
    'ship' : my_file_directory / 'ship.jpg'
}


#making a fancy print of my hash files
for key in hash_objects:
    ho = hash_objects[key]                         # assigning a common variable name because I am lazy
    print(f'Directory: {ho.parent}')               # path_object.parent is the directory without the file name
    print(f'File name: {hash_objects[key].name}')  # path_object.name is the name and extension
    print(f'hash: {make_hash(hash_objects[key])}') # hashing file