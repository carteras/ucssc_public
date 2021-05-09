from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('square', type=int, help="display a square of a given number")
parser.add_argument("-v", "--verbosity", help="increase output verbosity", action="store_true")
args = parser.parse_args()
if args.verbosity:
    print(f"The square of {args.square} equals {args.square**2}")
else:
    print(args.square**2)