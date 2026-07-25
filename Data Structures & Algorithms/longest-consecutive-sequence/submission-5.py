class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        res = 0
        temp_res = 0
        nums_set = set(nums)
        for num in nums_set:
            if num-1 in nums_set:
                continue
            else:
                while num+1 in nums_set:
                    temp_res += 1
                    num += 1
                if temp_res > res:
                    res = temp_res
                temp_res = 0
        return res + 1


        