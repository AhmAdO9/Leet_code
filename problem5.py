class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        j=1
        out = {}
        for i in nums:
            count = 1
            try:    
                if i == nums[j]:    
                    while i == nums[j]:
                        nums.pop(j)
                        count=count+1
                    out[i]=count  
                    j+=1      
                else:
                    count = 1
                    out[i]=count
                    j+=1    
            except IndexError:
                 out[i]=count
        keys = list(out.keys())
        val = list(out.values())
        
        # return keys[val.index(max(val))]
        return out
    


            
nums = [1,1,2,3,4,4,4,4,5,5,5,5,55,6,6,6]
sol = Solution()
print(sol.majorityElement(nums))