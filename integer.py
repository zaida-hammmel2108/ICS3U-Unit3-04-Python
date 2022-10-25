#!/usr/bin/env python3

# Created by: Zaida Hammel
# Created on: Oct 2022
# This program identifies your integer


def main():
    # This function determines if your integer is positive, negative or neither.

    # input
    user_number = int(input("Enter any integer: "))

    # process
    if user_number < 0:
        # output
        print("{0} is a negative integer!".format(user_number))
    elif user_number > 0:
        # output
        print("{0} is a positive integer!.".format(user_number))
    else:
        # output
        print("{0} is just zero!.".format(user_number))

    print("")
    print("\nDone.")


if __name__ == "__main__":
    main()
