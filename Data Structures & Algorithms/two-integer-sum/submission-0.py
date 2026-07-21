class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {} # key: difference | value: index
        answer = []
        for i in range(len(nums)):
            if nums[i] in res:
                return [res[nums[i]], i]
            else:
                res[target-nums[i]] = i
        
        