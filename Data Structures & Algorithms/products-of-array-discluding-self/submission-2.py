import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = math.prod(nums)        
        res = []

        for num in nums:
            if num == 0:
                nums_copy = nums.copy()
                nums_copy.remove(num)
                res.append(int(math.prod(nums_copy)))                
            else:
                res.append(int(product/num))

        return res