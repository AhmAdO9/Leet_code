#!/bin/python3

import math
import os
import random
import re
import sys


def plusMinus(arr):
    pos = []
    neg = []
    zeroes = []
    for i in arr:
        if (i * -1) > 0 :
            neg.append(i)
        elif (i*-1) < 0:
            pos.append(i)
        else:
            zeroes.append(i)
    
    print("%.7f" % (len(pos)/x))
    print("%.7f" % (len(neg)/x))
    print("%.7f" % (len(zeroes)/x))
    
x = int(input(""))
y = input().split(" ")


if __name__ == '__main__':
    p =1
    arr_new = []
    for i in y:
        arr_new.append(int(i))
    plusMinus(arr_new)
