from ensure import ensure_annotations


@ensure_annotations
def fibonacci(N: int):
    i = 1
    arr = []
    a = 0
    b=1
    while i < N:
        c = a+b
        if c % 2 == 0:
            arr.append(c)
        a=b
        b=c
        i+=1    
    li = filter(lambda x: x<N, arr)
    ar = [i for i in li]
    return ar


print(fibonacci(100))