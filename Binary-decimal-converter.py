#!/usr/bin/env python3

binary = input("Enter a binary number please: ")

i = 0
while i < len(binary):
    if int(binary[i]) > 1:
        check = False
    else:
        check = True
    i = i + 1

if check == False:
    binary = input("Not a binary number try again: ")

total = 0

i = 0
while i < len(binary):
    total = total + (int(binary[len(binary) - i - 1]) * (2 ** i))
    i = i + 1
 
print("The decimal equivalent is:", total)