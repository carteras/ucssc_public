from argparse import ArgumentParser
parser = ArgumentParser()

# parser.add_argument("echo", help="Echos the string that you entered")
parser.add_argument('square', help='Squares the given number', type=int)

parser.add_argument(
    '-w',
    '--wordy', 
    help='increases the wordyness of the answer',
    action='store_true'
)

args = parser.parse_args()

print(args)
if args.wordy:
    print(f'{args.square}**2=={args.square**2}')
else:
    print(args.square**2)