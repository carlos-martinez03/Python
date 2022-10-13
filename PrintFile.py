# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def PrintFile(name=""):
    if name == "":
        return "File no defined"

    print("----------------------------------------------")
    print()
    f = open(name, "rt")
    Count = 0
    for line in f:
        print(line.rstrip())
        Count += 1
    print()
    print("----------------------------------------------")
    print(f"File name: {name} has {Count} line(s)")


def main():
    PrintFile("Plot.py")


if __name__ == "__main__":
    main()
