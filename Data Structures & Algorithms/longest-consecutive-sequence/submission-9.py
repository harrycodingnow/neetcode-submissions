class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        res = 0
        num_set = set()
        
        for i in range(len(nums)):
            num_set.add(nums[i])
        
        for j in range(len(nums)): 
            temp_res = 0           
            if nums[j] - 1 not in num_set:
                while nums[j] + 1 in num_set:
                    nums[j] += 1
                    temp_res += 1
                    
                                
            res = max(res, temp_res)
        
        return res + 1


        
        

        