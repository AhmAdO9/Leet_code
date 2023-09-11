def mergeArray(num1,num2):
    out = []
    for i in num1:
        if i != 0:
            out.append(i)
    num1 = out+num2
    num1.sort()
    return num1

print(mergeArray([1,0,2,3,0,0,0,0],[6,7,8]))

