class Solution():
    def removeDuplicates_LevelTwo(self, nums):
        out = []
        nums.sort()
        j=1
        for i in nums:
            out.append(i)
            count = 0
            try:
                if i == nums[j]:
                    while i == nums[j]:
                        count+=1
                        if count>=2:
                         nums.pop(j)
                        else:
                             j+=1
                else:
                    j+=1
            except IndexError:
                pass
        return out

nums = [1,1,1,1,1,1,2,2,7,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]
sol = Solution() 
print(sol.removeDuplicates_LevelTwo(nums))
