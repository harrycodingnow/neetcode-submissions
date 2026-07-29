class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: 
        if len(nums) < 1:
            return 0
            
        num_set = set(nums)
        res = 0
        for num in nums:
            temp_res = 0
            if num - 1 in num_set:
                continue
            else:
                while num + 1 in num_set:
                    temp_res += 1
                    num += 1                    
                res = max(res, temp_res)

        return res + 1


