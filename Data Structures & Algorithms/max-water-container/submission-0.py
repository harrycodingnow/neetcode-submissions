class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0        
        left = 0
        right = len(heights) - 1
        while right > left:
            temp_res = min(heights[right], heights[left]) * (right-left)
            if temp_res > res:
                res = temp_res
            if heights[left] > heights[right]:
                right -= 1
            elif heights[right] > heights[left]:
                left += 1
            else:
                left += 1
        return res
