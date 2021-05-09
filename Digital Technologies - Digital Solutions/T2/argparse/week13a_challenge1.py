from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('string_in',help="words to capitalize")
parser.add_argument("-v", "--verbosity", help="increase output verbosity", action="store_true")
group = parser.add_mutually_exclusive_group()
group.add_argument("-l", "--lower", help="will send your word to lower case", action="store_true")
group.add_argument("-u", "--upper", help="will send your word to upper case", action="store_true")
group.add_argument("-c", "--capitalize", help="will send your word to capitalize case", action="store_true")
group.add_argument("-t", "--title", help="will send your word to title case", action="store_true")


args = parser.parse_args()
if args.upper:
    if args.string_in == args.string_in.upper():
        print('UNMODIFIED: ', args.string_in)
    else: 
        print('MODIFIED: ',args.string_in.upper())
elif args.capitalize:
    if args.string_in == args.string_in.capitalize():
        print('UNMODIFIED: ', args.string_in)
    else: 
        print('MODIFIED: ',args.string_in.capitalize())
elif args.title:
    if args.string_in == args.string_in.title():
        print('UNMODIFIED: ', args.string_in)
    else: 
        print('MODIFIED: ',args.string_in.title())
else:
    if args.string_in == args.string_in.lower():
        print('UNMODIFIED: ', args.string_in)
    else: 
        print('MODIFIED: ',args.string_in.lower())