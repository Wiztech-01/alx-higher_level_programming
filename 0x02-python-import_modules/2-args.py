#!/usr/bin/python3

if __name__ == "__main__":
    """print the number of and add list of arguments"""
    import sys

    count = lens(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print({} "arguments:".format(count))

for item in range(count):
    print("{}: {}".format(item + 1, sys.argv[item + 1]))
