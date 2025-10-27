import os  # list folders, check if something is a directory. os - module provides a portable way of using operating system dependent functionality.
import argparse  # read command-line flags. argparse - module makes it easy to write user-friendly command-line interfaces.
from pathlib import Path # pathlib is a Python standard library (built-in, no install needed) for working with file system paths

# set up argparse
parser = argparse.ArgumentParser()
parser.add_argument("-a", action="store_true")  # show hidden files
parser.add_argument("path", nargs="?", default=".")  # positional argument. Optional folder path
args = parser.parse_args()

# convert to absolute Path object
target = Path(args.path).resolve()

try:
    # List directories
    entries = os.listdir(target)

    result = []
    for name in entries:
        if args.a:
            # if -a flag is used, include everything
            result.append(name)
        else:
            # if no -a, skip hidden files
            if not name.startswith("."):
                result.append(name)

    result.sort()

    # print line by line
    for item in result:
        print(item)

except Exception as e:
    print("Error:", e)
