def fun(sequence):
    test = [1]
    if (sequence in test):
        return True
    else:
        return False

sequence = [1,2,3,4,5,6,7,8,9]
filtered = (filter(fun,sequence))
for  i in filtered:
    print(i)



List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]
 
# Sort each sublist
sortList = [lambda x: (sorted(i) for i in x)]
 
# Get the second largest element
secondLargest = lambda x, f : [y[len(y)-2] for y in f(x)]
res = secondLargest(List, sortList)
 
print(res)

