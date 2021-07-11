from argparse import ArgumentParser
from pathlib import Path

parser = ArgumentParser()
parser.add_argument(
    "directory1",
    nargs="?",
    default="forensics1",
    help="recursively reads all of the files in directory and sub-driectories and stores them to hashes",
)
parser.add_argument(
    "directory2",
    nargs="?",
    default="forensics2",
    help="recursively reads all of the files in directory and sub-driectories and stores them to hashes",
)
parser.add_argument("-s", "--save", help="saves the output to a given text file SAVE")

args = parser.parse_args()


def hash_file(path_object, algorithm="md5"):
    from hashlib import md5

    m = md5()
    with open(path_object, "rb") as fr:
        while chunk := fr.read(m.block_size):
            m.update(chunk)
    return m.hexdigest()


def walk(directory_name):
    for path_object in directory_name.glob("**/*"):
        if path_object.is_file():
            files_to_hash.append(path_object)
        elif path_object.is_dir():
            directories.insert(0, path_object)
    return files_to_hash


def detect_differences(files):
    files_to_hash = {}

    for f in files:
        if f.name in files_to_hash:
            temp_hash = hash_file(f)
            if files_to_hash[f.name]["digest"] != temp_hash:
                print(f"Anomalous File Detected!")
                print(f"File name:")
                print(f"\t{f.name}")
                print(f'\t{files_to_hash[f.name]["file"].name}')
                print("Hash Digests:")
                print(f"\t{temp_hash}")
                print(f'\t{files_to_hash[f.name]["digest"]}')
                print("Directories found in:")
                print(f'\t{files_to_hash[f.name]["file"].parent}')
                print(f"\t{f.parent}")
        else:
            files_to_hash[f.name] = {"digest": hash_file(f), "file": f}


base_path = Path.cwd()

dir1 = base_path / args.directory1
dir2 = base_path / args.directory2

directories = [dir1, dir2]
files_to_hash = []
while len(directories) > 0:
    directory = directories.pop(0)
    walk(directory)


detect_differences(files_to_hash)
