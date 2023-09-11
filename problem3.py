class Solution():
    def removeDuplicates(self, nums):
        out = []
        j=1
        nums.sort()
        for i in nums:
            out.append(i) 
            try:
                while i == nums[j]:
                    nums.pop(j)
                j+=1
            except IndexError:
                pass
        return out

nums = [1,1,2,3,3,5,5,6,6,7,7,8,8,9,9,9,9,9,9,9,9,4,4]
sol = Solution() 
print(sol.removeDuplicates(nums))

