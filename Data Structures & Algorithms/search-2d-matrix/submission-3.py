class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        target_row = []
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1] :
                target_row = matrix[i]

        left = 0
        right = len(target_row) - 1

        while left <= right:
            mid = (right+left)//2
            if target_row[mid] == target:
                return True
            elif target_row[mid] < target:
                left = mid + 1
            elif target_row[mid] > target:
                right = mid - 1

        return False
        


        
        