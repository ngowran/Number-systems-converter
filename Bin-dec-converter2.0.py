#!/usr/bin/env python3

def convert(number):
    total = 0

    for x in number:
        if x != "1" and x != "0":
            return("Please enter a vaild binary number")

    i = 0
    while i < len(number):
        total = total + (int(number[len(number) - i - 1]) * (2 ** i))
        i = i + 1
    return total


def main():
    try:
        number = input("Please enter the number you want to convert: ")
    except ValueError:
        print("Enter a vaild number please: ")
    print(f"The decimal equlivalent of {number} is: {convert(number)}")


if __name__ == '__main__':
    main()