#!/usr/bin/python3
def uppercase(str):
    result_str = ''
    for a in str:
        if ord(a) >= ord('a') and ord(a) <= ord('z'):
            result_str += chr(ord(a) - 32)
        else:
            result_str += a
    print("{0:s}".format(result_str))
