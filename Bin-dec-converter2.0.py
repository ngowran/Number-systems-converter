#!/usr/bin/env python3

def convert(number):
    total = 0
    i = 0
    while i < len(number):
        total = total + (int(number[len(number) - i - 1]) * (2 ** i))
        i = i + 1
    return total


def check_bin(n):
    for x in n:
        if x != "1" and x != "0":
            return False
    return True


def main():
    try:
        number = input("Please enter the number you want to convert: ")
        while check_bin(number) != True:
            number = input("Please enter a vaild binary number: ")

    except ValueError:
        print("Enter a vaild number please: ")
    print(f"The decimal equlivalent of {number} is: {convert(number)}")


if __name__ == '__main__':
    main()