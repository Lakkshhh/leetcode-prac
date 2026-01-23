class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            low = 0
            high = len(matrix[i])-1

            while low <= high:
                mid = low + (high-low)//2

                if target < matrix[i][mid]:
                    high = mid - 1
                elif target > matrix[i][mid]:
                    low = mid + 1
                else:
                    return True
        
        return False