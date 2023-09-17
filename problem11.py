class Solution(object):
    def canJump(self, nums):
        i = nums[0]
        n=1
        while True:
            try:
                j = nums[i]
            except IndexError:
                return False
            if j == 0:
                return False
            if i == len(nums)-1:
                print(n)
                return True
            i = i+j
            n+=1

sol = Solution()
print(sol.canJump([2,3,1,1,4]))

