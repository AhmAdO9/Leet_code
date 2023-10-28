from math import *

def splitString(string: str) -> bool:
    l = len(string)
    l2 = floor(l/2)
    l_st =  string[:l2]
    r_st = string[l2:]
    ls = 0
    rs = 0
    vovels = ['a','e','i','o','u','A','E','I','O','U']
    for i in vovels:
        for j,k in zip(l_st,r_st):
            if i == j:
                ls +=1
            if i == k:
                rs +=1

    if ls == rs:
        return True 
    else:
        return False


print(splitString("xXfmKYQLAbTArGwjAJ"))