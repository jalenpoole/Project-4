import argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Code to add two numbers")
	parser.add_argument('--lst', type=int, nargs='+', help="Second number to add")
	parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=sum,
                    help='sum the integers (default: find the max)')
	parser.add_argument('len', 
                    action ='store_const', 
                    const = len)
	args = parser.parse_args()
	print("Average: " + str(args.accumulate(args.lst)/args.len(args.lst)))