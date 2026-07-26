class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:                
        nums.sort()
        res = []
        for i in range(len(nums)):
            right = len(nums) - 1
            left = i + 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]                            
            while right > left:
                if nums[left] + nums[right] == target:
                    res.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left +=1
                elif nums[left] + nums[right] < target:                    
                    left += 1
                elif nums[left] + nums[right] > target:        
                    right -= 1                
        return res

                
        