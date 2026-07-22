import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = math.prod(nums)        
        res = []
        for num in nums:
            if num == 0:
                temp = nums.copy()
                temp.remove(num)
                res.append(int(math.prod(temp)))
            else:
                ans = int(product/num)
                res.append(ans)
        
        return res

        
        