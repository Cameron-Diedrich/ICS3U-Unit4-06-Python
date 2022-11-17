#!/usr/bin/env python3

# Created by: Cameron Diedrich
# Created on: Nov 2022
# This program finds every RGB


def main():
    # This function finds every valid RGB

    counter1 = 0
    counter2 = 0
    counter3 = 0

    # Process and Output
    for counter1 in range(256):
        for counter2 in range(256):
            for counter3 in range(256):
                print("RGB({0},{1},{2})".format(counter1, counter2, counter3))

    print("\nDone")


if __name__ == "__main__":
    main()
