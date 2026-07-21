class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = {}
        for num in nums:
            if num in res:
                return True
            else:
                res[num] = 1
        return False
            
        