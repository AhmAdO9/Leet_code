import functools

class Solution(object):
    def productExceptSelf(self, nums):
        orig = []
        k = -1
        for i in nums:
            k+=1    
            li = nums.copy()
            li.remove(i)
            j = functools.reduce(lambda x,y: x*y, li)
            orig.insert(k,j)
        return orig       


sol = Solution()
print(sol.productExceptSelf([-1,1,0,-3,3]))
