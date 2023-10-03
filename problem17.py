def countPairs(arr):
    orig = []
    l = 0
    j=1
    loop = 1
    j = loop
    for i in arr:
        if  j == 1:
            pass
        else:
            loop +=1
            j = loop
        while l <= len(arr):
            try:
                c = i&arr[j]
                if c == 0:
                    l+=1
                    j+=1
                    continue
                if c ==1 or c%2 ==0:
                    orig.append(2)
                    j+=1
                    l+=1
                else:
                    l+=1
                    j+=1
            except IndexError as e:
                l=0
                break

    print(len(orig))

