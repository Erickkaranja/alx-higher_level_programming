##!/usr/bin/python3
# 1-calculation.py

'''if __name__ == "__main__":
    """Print the sum, difference, multiple and quotient of 10 and 5."""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    print(f'{a} + {b} = {add(a, b)}')
    print(f'{a} - {b} = {sub(a, b)}')
    print(f'{a} * {b} = {mul(a, b)}')
    print(f"{a} / {b} = {div(a, b)}")'''
#!/usr/bin/python3
# 1-calculation.py
# Brennan D Baraban <375@holbertonschool.com>

if __name__ == "__main__":
    """Print the sum, difference, multiple and quotient of 10 and 5."""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
