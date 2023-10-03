import functools

def filledOrders(order, k):
    total = functools.reduce(lambda x,y: x+y,order)
    if total <= k:
        return(len(order))
    elif min(order) > k:
        return 0
    elif k in order:
        return 1
    
    maxy = []
    dummy = order.copy()
    for i in order:
        orig = [i]    
        for j in dummy:    
                orig.append(j)
                total = functools.reduce(lambda x,y: x+y,orig)
                if total > k:
                    l = len(orig)
                    orig.pop(l-1)
                elif total < k:
                     continue
                elif total == k:
                    save = len(orig)
                    if len(dummy) != 1:
                        orig.pop(l-1)          
        dummy.remove(i)
    if save > len(orig):
        maxy.append(save)
    else:
        maxy.append(len(orig))
    return max(maxy)


print(filledOrders([5,3,3,1,1,1],6))