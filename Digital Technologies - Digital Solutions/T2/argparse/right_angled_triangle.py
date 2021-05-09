# create a program that solves pythagoras triangles
# a^2 + b^2 = c^2 
# 3^2 + 4^2 = c^2
# 9 + 16 = c^2
# 25 = c^2
# 5 = c 
# a	=	side of right triangle
# b	=	side of right triangle
# c	=	hypotenuse
# use all optional parameters 
# if all three sides are given solves if the triangle is a right angle triangle 

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('a', help="One side of a right angle triangle")
parser.add_argument('b', help="One side of a right angle triangle")
parser.add_argument('c', help="The hypotenuse of a right angle triangle")
args = parser.parse_args()
print(args)

if args.a.isnumeric():
    a = args.a

if args.a and args.b and args.c:
    if args.a**2 + args.b**2 == args.c**2:
        print(f"Hey, {args.a} {args.b} {args.c} is right angle triangle!")
    else:
        print(f"Hey, {args.a} {args.b} {args.c} is not right angle triangle!")
elif args.a and args.b:
    c2 = args.a**2 + args.b**2
    print(f"C = {c2**0.5}")
elif args.b and args.c:
    a2 = args.c**2 - args.b**2
    print(f"B = {a2**0.5}")
elif args.a and args.c:
    b2 = args.c**2 - args.a**2
    print(f"B = {b2**0.5}")
else:
    print("Hey, you might need to run this file with -h so you know how it works!")


