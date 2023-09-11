def Solution(weights):
    j = 0 
    n = 0
    if len(weights) < 5:
        i = len(weights)
        while i < 5: 
            weights.append(0)
            i+=1
    for i in range(5):
        output = weights.copy()
        val = output.pop(j)
        if output[2*n]+output[(2*n)+2] == output[(2*n)+1]+output[(2*n)+3]:
            break
        j+=1
    return val, output
print(Solution([3,3,3]))                   