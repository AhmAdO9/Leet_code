import math

def hIndex(citations):
    d = {}
    j = 1
    for i in citations:
        if i == 0 :
            continue
        for j in citations:
            try:
                if i <= j:
                    d[i] = d[i]+1
            except KeyError:
                    d[i] = 1

    orig = []
    for i in d :
        if d[i] > math.floor(len(d)/2):
             orig.append(i)
    while True:
        y = max(orig)
        try:
             citations[y-1]
             return y
        except IndexError:
             orig.pop(orig.index(y))


s = hIndex([4,4,4,4,4,4,5])

print(s)