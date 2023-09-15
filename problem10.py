import operator, functools

class Solution(object):
    def minCostConnectPoints(self, points): 
        orig = {}
        for  i in  points:
            my_list = []
            for j in points:
                if j == i:
                    continue
                ans = abs(i[0]-j[0]) + abs(i[1]-j[1]) 
                my_list.append(ans)
            if points.index(i) <= my_list.index(min(my_list)):        
                n =  my_list.index(min(my_list))+1
            else:
                n =  my_list.index(min(my_list))
            try:
                orig[f"{points[n], i}"]
            except KeyError:
                orig[f"{i,points[n]}"] = min(my_list)
        lis = list(orig.values())
        return functools.reduce(operator.add,lis )
    

sol = Solution()
print(sol.minCostConnectPoints([[3,12],[-2,5],[-4,1]]))
        
        