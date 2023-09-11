class Solution():
    def removeElement(self, nums, val):
        out = []
        empty = []
        for i in nums:
            if i == val:
                empty.append("_")
            else:
                out.append(i)
        return out+empty
                
                            
nums = [1,2,3,4,5,2,2,3]
sol = Solution()
print(sol.removeElement(nums, 2))
