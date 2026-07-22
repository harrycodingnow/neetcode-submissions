class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        temp = nums.copy()
        res = set(temp)
        temp_count = 1
        final_count = 1
        for num in nums:
            if num-1 in res:
                continue
            else:
                while num+1 in res:
                    temp_count += 1
                    num += 1
                if temp_count >= final_count:
                    final_count = temp_count
                    temp_count = 1
            temp_count = 1
        return final_count


            

        