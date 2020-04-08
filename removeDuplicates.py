import sys
import argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--lst','--list', nargs='+', help='<Required> Set flag', required=True)
	parser.add_argument('len', 
                    action ='store_const', 
                    const = len)
	args = parser.parse_args()

	for i in args.lst:
		result = ''
		for x in i:
			if not(x in result):
				result += x
		print(result)
