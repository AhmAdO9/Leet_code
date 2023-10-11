from ensure import ensure_annotations
import functools


@ensure_annotations
def Euler(N: int)->int:
    arr = []
    for i in range(1, N):
        if (i % 3)==0 or (i % 5)==0:
            arr.append(i)
    value = functools.reduce(lambda x, y: x+y, arr)
    return value


print(Euler(100))