#!/usr/bin/python3
import sys
import calculator_1 as calc
if __name__ == "__main__":
    operators = {'+': calc.add, '-': calc.sub, '*': calc.mul, '/': calc.div}
    if len(sys.argv) != 4:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if sys.argv[2] != "+" and sys.argv[2] != "-"\
       and sys.argv[2] != "*" and sys.argv[2] != "/":
        print(f"Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    for op, func in operators.items():
        if sys.argv[2] == op:
            result = operators[op](int(sys.argv[1]), int(sys.argv[3]))
            print(f"{sys.argv[1]:s} {sys.argv[2]:s} {sys.argv[3]:s} = \
{result:d}")
