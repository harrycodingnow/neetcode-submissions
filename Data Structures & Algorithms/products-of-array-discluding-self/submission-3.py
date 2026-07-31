class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = math.prod(nums)
        res = []
        for i in range(len(nums)):
            if nums[i] == 0:
                temp = nums.copy()
                temp.remove(temp[i])
                temp_product = math.prod(temp)
                res.append(int(temp_product))
            else:
                res.append(int(product/nums[i]))
        return res
                

        