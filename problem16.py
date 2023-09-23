class Solution(object):
    def candy(self, ratings):
        amount = []
        j = 0
        for i in ratings:
            if j == 0:
                amount.append(1)
                j+=1
                continue
            if i > ratings[j-1]:
                amount.append(amount[j-1]+1)
                j+=1
            elif i < ratings[j-1]:
                amount[j-1]= amount[j-1]+1
                amount.append(amount[j-1]-1)
                j+=1
            else:
                amount.append(amount[j-1]-1)
                j+=1

        print(amount) 

sol = Solution()
sol.candy([1,2,2])