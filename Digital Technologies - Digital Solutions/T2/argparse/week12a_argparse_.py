from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('echo', help='Repeats text string given')

args = parser.parse_args()
print(args.echo)