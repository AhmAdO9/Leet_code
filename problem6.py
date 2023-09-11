class Solution(object):
    def rotate(self, nums, k):
        try:    
            j=1
            if k > len(nums)  or k < j:
                raise IndexError
            out = []
            sorted_arr = sorted(nums,reverse=True)
            for i in sorted_arr:
                if j > k :
                    break  
                out.append(i)
                last_index = len(nums)-1
                nums.pop(last_index)
                j+=1
        except IndexError:
            return "Please choose a suitable value for k !"
        return out+nums
    
nums = [1,2,3,4,5,6]

sol = Solution()

print(sol.rotate(nums,k=1))

