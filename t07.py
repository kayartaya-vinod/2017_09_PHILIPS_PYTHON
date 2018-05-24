### ------------ command line arguments in Python ------------
import sys, getopt

opts, args = getopt.getopt(sys.argv[1:], "ab:c:d")
print(opts)
print(args)
print("-"*50)
for opt, arg in opts:
	print(opt, arg)

### ------------ command line arguments in Python ------------

