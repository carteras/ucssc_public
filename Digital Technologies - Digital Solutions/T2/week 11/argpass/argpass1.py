import pathlib
import argparse

parser = argparse.ArgumentParser(description='Moves files around')
parser.add_argument('--list', default=False, help='copies files from input directory to output')
args = parser.parse_args()
print(args.list)
print('> HEY LOOK HERE ->',pathlib.Path.cwd())
if args.list == True:
    pass
