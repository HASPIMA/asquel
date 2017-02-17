import parser
from math import *

def main():
    while True:
        try:
            # To run under Python3 replace 'raw_input' call
            # with 'input'
            text = raw_input('calc> ')
        except EOFError:
            break
        if not text:
            continue

	formula = text
	code = parser.expr(formula).compile()
	x = 10
	print eval(code)


if __name__ == '__main__':
    main()
