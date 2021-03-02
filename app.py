#!/bin/python3

import sys
import progresspie


def main(argv):
    is_black = progresspie.is_black(int(argv[0]), int(argv[1]), int(argv[2]))
    print("black" if is_black else "white")


if __name__ == "__main__":
    main(sys.argv[1:])
