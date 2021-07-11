from pathlib import Path
from argparse import ArgumentParser
parser = ArgumentParser()

parser.add_argument('file_name', help='recursively reads all of the files in directory and sub-directories and stores them to hashes')
parser.add_argument('-r', '--read', action="store_true", help='writes a file to standard outputS')
args = parser.parse_args()

print(args)

file = Path().cwd() / args.file_name

if args.read:
    with open(file) as fr:
        for line in fr:
            print(line, end='')
else: 
    if not file.is_file():
        print(f"{file} does not exist")