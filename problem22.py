import functools
from ensure import ensure_annotations



@ensure_annotations
def prime_factors(N:int):
    arr=[]
    li = [2,3,5,7]
    for i in range(4,N):
        if N in li:
            return N
        elif (N % i == 0) and i not in li:
            arr.append(i) 

    if arr == []:
        j = 1
        while arr == []:
            if N % li[len(li)-j] == 0:
                arr.append(li[len(li)-j])
                return arr[0]
            else:
                if j == len(li)-1:
                    return N
                else :
                    j+=1
    return arr

print(prime_factors(17))

