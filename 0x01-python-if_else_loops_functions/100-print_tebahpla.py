#!/usr/bin/python3
for char in range(ord('z'), ord('a') - 1, -1):
    if char % 2 != 0:
        print(f"{chr(char - 32):s}", end='')
    else:
        print(f"{chr(char):s}", end='')
